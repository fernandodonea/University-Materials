using System.Net.Http.Headers;
using System.Text;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace ArticlesApp.Services
{
    // Clasa pentru rezultatul analizei de sentiment
    public class SentimentResult
    {
        public string Label { get; set; } = "neutral";  // positive, neutral, negative
        public double Confidence { get; set; } = 0.0;   // 0.0 - 1.0
        public bool Success { get; set; } = false;
        public string? ErrorMessage { get; set; }
    }

    // Interfata serviciului pentru dependency injection
    public interface ISentimentAnalysisService
    {
        Task<SentimentResult> AnalyzeSentimentAsync(string text);
    }

    // Implementarea serviciului de analiza sentiment folosind OpenAI API
    public class SentimentAnalysisService : ISentimentAnalysisService
    {
        private readonly HttpClient _httpClient;
        private readonly string _apiKey;
        private readonly ILogger<SentimentAnalysisService> _logger;

        public SentimentAnalysisService(IConfiguration configuration, ILogger<SentimentAnalysisService> logger)
        {
            _httpClient = new HttpClient();
            _apiKey = configuration["OpenAI:ApiKey"] ?? throw new ArgumentNullException("OpenAI:ApiKey not configured");
            _logger = logger;

            // Configurare HttpClient pentru OpenAI API
            _httpClient.BaseAddress = new Uri("https://api.openai.com/v1/");
            _httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", _apiKey);
            _httpClient.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
        }

        public async Task<SentimentResult> AnalyzeSentimentAsync(string text)
        {
            try
            {
                // Construim prompt-ul pentru analiza de sentiment
                var systemPrompt = @"You are a sentiment analysis assistant. Analyze the sentiment of the given text and respond ONLY with a JSON object in this exact format:
{""label"": ""positive|neutral|negative"", ""confidence"": 0.0-1.0}

Rules:
- label must be exactly one of: positive, neutral, negative
- confidence must be a number between 0.0 and 1.0
- Do not include any other text, only the JSON object";

                var userPrompt = $"Analyze the sentiment of this comment: \"{text}\"";

                // Construim request-ul pentru OpenAI API
                var requestBody = new
                {
                    model = "gpt-4o-mini",  // Using gpt-4o-mini as gpt-5-nano doesn't exist
                    messages = new[]
                    {
                        new { role = "system", content = systemPrompt },
                        new { role = "user", content = userPrompt }
                    },
                    temperature = 0.1,  // Low temperature for consistent results
                    max_tokens = 50
                };

                var jsonContent = JsonSerializer.Serialize(requestBody);
                var content = new StringContent(jsonContent, Encoding.UTF8, "application/json");

                _logger.LogInformation("Sending sentiment analysis request to OpenAI API");

                // Trimitem request-ul catre OpenAI API
                var response = await _httpClient.PostAsync("chat/completions", content);
                var responseContent = await response.Content.ReadAsStringAsync();

                if (!response.IsSuccessStatusCode)
                {
                    _logger.LogError("OpenAI API error: {StatusCode} - {Content}", response.StatusCode, responseContent);
                    return new SentimentResult
                    {
                        Success = false,
                        ErrorMessage = $"API Error: {response.StatusCode}"
                    };
                }

                // Parsam raspunsul de la OpenAI
                var openAiResponse = JsonSerializer.Deserialize<OpenAiResponse>(responseContent);
                var assistantMessage = openAiResponse?.Choices?.FirstOrDefault()?.Message?.Content;

                if (string.IsNullOrEmpty(assistantMessage))
                {
                    return new SentimentResult
                    {
                        Success = false,
                        ErrorMessage = "Empty response from API"
                    };
                }

                _logger.LogInformation("OpenAI response: {Response}", assistantMessage);

                // Parsam JSON-ul din raspunsul asistentului
                var sentimentData = JsonSerializer.Deserialize<SentimentResponse>(assistantMessage);

                if (sentimentData == null)
                {
                    return new SentimentResult
                    {
                        Success = false,
                        ErrorMessage = "Failed to parse sentiment response"
                    };
                }

                // Validam si normalizam label-ul
                var label = sentimentData.Label?.ToLower() switch
                {
                    "positive" => "positive",
                    "negative" => "negative",
                    _ => "neutral"
                };

                // Validam confidence score
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
                _logger.LogError(ex, "Error analyzing sentiment");
                return new SentimentResult
                {
                    Success = false,
                    ErrorMessage = ex.Message
                };
            }
        }
    }

    // Clase pentru deserializarea raspunsului OpenAI
    public class OpenAiResponse
    {
        [JsonPropertyName("choices")]
        public List<Choice>? Choices { get; set; }
    }

    public class Choice
    {
        [JsonPropertyName("message")]
        public Message? Message { get; set; }
    }

    public class Message
    {
        [JsonPropertyName("content")]
        public string? Content { get; set; }
    }

    public class SentimentResponse
    {
        [JsonPropertyName("label")]
        public string? Label { get; set; }

        [JsonPropertyName("confidence")]
        public double Confidence { get; set; }
    }
}
