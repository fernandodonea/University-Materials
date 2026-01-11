using System.Net.Http.Headers;
using System.Text;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace ArticlesApp.Services
{
    // =====================================================================
    // SERVICIU DE ANALIZĂ SENTIMENT FOLOSIND GOOGLE AI (GEMINI)
    // =====================================================================
    //
    // Acest fișier conține implementarea serviciului de analiză sentiment
    // folosind Google Generative AI (Gemini) în loc de OpenAI.
    //
    // PAȘI PENTRU A SCHIMBA DE LA OPENAI LA GOOGLE AI:
    // =====================================================================
    //
    // 1. În fișierul appsettings.json, adăugați configurația pentru Google AI:
    //
    //    "GoogleAI": {
    //        "ApiKey": "CHEIA_TA_API_GOOGLE"
    //    }
    //
    // 2. În fișierul Program.cs, schimbați înregistrarea serviciului:
    //
    //    // ÎNAINTE (OpenAI):
    //    // builder.Services.AddScoped<ISentimentAnalysisService, SentimentAnalysisService>();
    //
    //    // DUPĂ (Google AI):
    //    builder.Services.AddScoped<ISentimentAnalysisService, GoogleSentimentAnalysisService>();
    //
    // 3. Asigurați-vă că aveți o cheie API validă de la Google AI Studio:
    //    https://aistudio.google.com/app/apikey
    //
    // =====================================================================

    /// <summary>
    /// Implementarea serviciului de analiză sentiment folosind Google AI (Gemini)
    /// Această clasă implementează aceeași interfață ISentimentAnalysisService
    /// pentru a permite schimbarea ușoară între provideri (OpenAI/Google)
    /// </summary>
    public class GoogleSentimentAnalysisService : ISentimentAnalysisService
    {
        private readonly HttpClient _httpClient;
        private readonly string _apiKey;
        private readonly ILogger<GoogleSentimentAnalysisService> _logger;

        // URL-ul de bază pentru API-ul Google Generative AI
        private const string BaseUrl = "https://generativelanguage.googleapis.com/v1beta/models/";

        // Modelul folosit - gemini-2.5-flash-lite
        private const string ModelName = "gemini-2.5-flash-lite";

        public GoogleSentimentAnalysisService(IConfiguration configuration, ILogger<GoogleSentimentAnalysisService> logger)
        {
            _httpClient = new HttpClient();

            // Citim cheia API din configurație
            // Asigurați-vă că ați adăugat "GoogleAI:ApiKey" în appsettings.json
            _apiKey = configuration["GoogleAI:ApiKey"]
                ?? throw new ArgumentNullException("GoogleAI:ApiKey nu este configurat în appsettings.json");

            _logger = logger;

            // Configurare HttpClient pentru Google AI API
            _httpClient.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
        }

        /// <summary>
        /// Analizează sentimentul unui text folosind Google AI (Gemini)
        /// </summary>
        /// <param name="text">Textul de analizat</param>
        /// <returns>Rezultatul analizei de sentiment</returns>
        public async Task<SentimentResult> AnalyzeSentimentAsync(string text)
        {
            try
            {
                // Construim prompt-ul pentru analiza de sentiment
                // Același format ca la OpenAI pentru consistență
                var prompt = $@"You are a sentiment analysis assistant. Analyze the sentiment of the given text and respond ONLY with a JSON object in this exact format:
{{""label"": ""positive|neutral|negative"", ""confidence"": 0.0-1.0}}

Rules:
- label must be exactly one of: positive, neutral, negative
- confidence must be a number between 0.0 and 1.0
- Do not include any other text, only the JSON object

Analyze the sentiment of this comment: ""{text}""";

                // Construim request-ul pentru Google AI API
                // Structura este diferită față de OpenAI - folosim "contents" și "parts"
                var requestBody = new GoogleAiRequest
                {
                    Contents = new List<GoogleAiContent>
                    {
                        new GoogleAiContent
                        {
                            Parts = new List<GoogleAiPart>
                            {
                                new GoogleAiPart { Text = prompt }
                            }
                        }
                    },
                    // Configurări pentru generare - temperature scăzută pentru rezultate consistente
                    GenerationConfig = new GoogleAiGenerationConfig
                    {
                        Temperature = 0.1,
                        MaxOutputTokens = 100
                    }
                };

                var jsonContent = JsonSerializer.Serialize(requestBody, new JsonSerializerOptions
                {
                    PropertyNamingPolicy = JsonNamingPolicy.CamelCase
                });

                var content = new StringContent(jsonContent, Encoding.UTF8, "application/json");

                // Construim URL-ul complet cu cheia API ca parametru
                // Google AI folosește X-goog-api-key sau parametru în URL
                var requestUrl = $"{BaseUrl}{ModelName}:generateContent?key={_apiKey}";

                _logger.LogInformation("Trimitem cererea de analiză sentiment către Google AI API");

                // Trimitem request-ul către Google AI API
                var response = await _httpClient.PostAsync(requestUrl, content);
                var responseContent = await response.Content.ReadAsStringAsync();

                if (!response.IsSuccessStatusCode)
                {
                    _logger.LogError("Eroare Google AI API: {StatusCode} - {Content}", response.StatusCode, responseContent);
                    return new SentimentResult
                    {
                        Success = false,
                        ErrorMessage = $"Eroare API: {response.StatusCode}"
                    };
                }

                // Parsăm răspunsul de la Google AI
                var googleResponse = JsonSerializer.Deserialize<GoogleAiResponse>(responseContent, new JsonSerializerOptions
                {
                    PropertyNameCaseInsensitive = true
                });

                // Extragem textul din răspuns
                // Structura: candidates[0].content.parts[0].text
                var assistantMessage = googleResponse?.Candidates?.FirstOrDefault()?.Content?.Parts?.FirstOrDefault()?.Text;

                if (string.IsNullOrEmpty(assistantMessage))
                {
                    return new SentimentResult
                    {
                        Success = false,
                        ErrorMessage = "Răspuns gol de la API"
                    };
                }

                _logger.LogInformation("Răspuns Google AI: {Response}", assistantMessage);

                // Curățăm răspunsul de eventuale caractere markdown (```json ... ```)
                var cleanedResponse = CleanJsonResponse(assistantMessage);

                // Parsăm JSON-ul din răspunsul asistentului
                var sentimentData = JsonSerializer.Deserialize<SentimentResponse>(cleanedResponse);

                if (sentimentData == null)
                {
                    return new SentimentResult
                    {
                        Success = false,
                        ErrorMessage = "Nu s-a putut parsa răspunsul sentiment"
                    };
                }

                // Validăm și normalizăm label-ul
                var label = sentimentData.Label?.ToLower() switch
                {
                    "positive" => "positive",
                    "negative" => "negative",
                    _ => "neutral"
                };

                // Validăm confidence score
                var confidence = Math.Clamp(sentimentData.Confidence, 0.0, 1.0);

                return new SentimentResult
                {
                    Label = label,
                    Confidence = confidence,
                    Success = true
                };
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Eroare la analiza sentimentului");
                return new SentimentResult
                {
                    Success = false,
                    ErrorMessage = ex.Message
                };
            }
        }

        /// <summary>
        /// Curăță răspunsul JSON de eventuale caractere markdown
        /// Gemini poate returna răspunsul înconjurat de ```json ... ```
        /// </summary>
        private string CleanJsonResponse(string response)
        {
            var cleaned = response.Trim();

            // Eliminăm blocurile de cod markdown dacă există
            if (cleaned.StartsWith("```json"))
            {
                cleaned = cleaned.Substring(7);
            }
            else if (cleaned.StartsWith("```"))
            {
                cleaned = cleaned.Substring(3);
            }

            if (cleaned.EndsWith("```"))
            {
                cleaned = cleaned.Substring(0, cleaned.Length - 3);
            }

            return cleaned.Trim();
        }
    }

    // =====================================================================
    // CLASE PENTRU SERIALIZAREA/DESERIALIZAREA RĂSPUNSURILOR GOOGLE AI
    // =====================================================================
    //
    // Structura request-ului Google AI:
    // {
    //   "contents": [
    //     {
    //       "parts": [
    //         { "text": "..." }
    //       ]
    //     }
    //   ]
    // }
    //
    // Structura răspunsului Google AI:
    // {
    //   "candidates": [
    //     {
    //       "content": {
    //         "parts": [
    //           { "text": "..." }
    //         ]
    //       }
    //     }
    //   ]
    // }
    // =====================================================================

    /// <summary>
    /// Clasa pentru request-ul către Google AI
    /// </summary>
    public class GoogleAiRequest
    {
        [JsonPropertyName("contents")]
        public List<GoogleAiContent> Contents { get; set; } = new();

        [JsonPropertyName("generationConfig")]
        public GoogleAiGenerationConfig? GenerationConfig { get; set; }
    }

    /// <summary>
    /// Conținutul mesajului pentru Google AI
    /// </summary>
    public class GoogleAiContent
    {
        [JsonPropertyName("parts")]
        public List<GoogleAiPart> Parts { get; set; } = new();
    }

    /// <summary>
    /// O parte din conținut (text, imagine, etc.)
    /// </summary>
    public class GoogleAiPart
    {
        [JsonPropertyName("text")]
        public string Text { get; set; } = string.Empty;
    }

    /// <summary>
    /// Configurări pentru generarea răspunsului
    /// </summary>
    public class GoogleAiGenerationConfig
    {
        [JsonPropertyName("temperature")]
        public double Temperature { get; set; } = 0.7;

        [JsonPropertyName("maxOutputTokens")]
        public int MaxOutputTokens { get; set; } = 1024;
    }

    /// <summary>
    /// Răspunsul de la Google AI API
    /// </summary>
    public class GoogleAiResponse
    {
        [JsonPropertyName("candidates")]
        public List<GoogleAiCandidate>? Candidates { get; set; }
    }

    /// <summary>
    /// Un candidat din răspuns (Google AI poate returna mai mulți candidați)
    /// </summary>
    public class GoogleAiCandidate
    {
        [JsonPropertyName("content")]
        public GoogleAiContent? Content { get; set; }
    }
}
