using ArticlesApp.Data;
using ArticlesApp.Models;
using Microsoft.AspNetCore.Identity;
using Microsoft.EntityFrameworkCore;

namespace ArticlesApp;

public static class SeedScript
{
    public static async Task RunAsync(IServiceProvider serviceProvider)
    {
        using var context = new ApplicationDbContext(
            serviceProvider.GetRequiredService<DbContextOptions<ApplicationDbContext>>());

        var userManager = serviceProvider.GetRequiredService<UserManager<ApplicationUser>>();

        // Check if user already exists
        var existingUser = await userManager.FindByEmailAsync("alex@codesilk.com");
        if (existingUser != null)
        {
            Console.WriteLine("User alex@codesilk.com already exists.");
            return;
        }

        // Add Categories if not exist
        List<Category> categories;
        if (!await context.Categories.AnyAsync())
        {
            categories = new List<Category>
            {
                new Category { CategoryName = "Tehnologie" },
                new Category { CategoryName = "Stiinta" },
                new Category { CategoryName = "Cultura" },
                new Category { CategoryName = "Sport" }
            };
            context.Categories.AddRange(categories);
            await context.SaveChangesAsync();
            Console.WriteLine("Categories added.");
        }
        else
        {
            categories = await context.Categories.ToListAsync();
            Console.WriteLine("Categories already exist.");
        }

        // Create user alex@codesilk.com
        var user = new ApplicationUser
        {
            UserName = "alex@codesilk.com",
            Email = "alex@codesilk.com",
            EmailConfirmed = true,
            FirstName = "Alex",
            LastName = "CodeSilk"
        };

        // Password must have: uppercase, digit, special char
        var result = await userManager.CreateAsync(user, "Parolamea1!");
        if (result.Succeeded)
        {
            await userManager.AddToRoleAsync(user, "User");
            Console.WriteLine("User alex@codesilk.com created.");
        }
        else
        {
            Console.WriteLine("Failed to create user: " + string.Join(", ", result.Errors.Select(e => e.Description)));
            return;
        }

        // Add Articles
        var articles = new List<Article>
        {
            new Article
            {
                Title = "Inteligenta Artificiala in 2024",
                Content = "Inteligenta artificiala continua sa revolutioneze industria tehnologica. De la asistenti virtuali la masini autonome, AI transforma modul in care interactionam cu tehnologia. Companiile investesc miliarde in cercetare si dezvoltare pentru a crea sisteme mai inteligente si mai eficiente.",
                Date = DateTime.Now,
                CategoryId = categories[0].Id,
                UserId = user.Id
            },
            new Article
            {
                Title = "Descoperiri recente in astronomie",
                Content = "Telescopul James Webb continua sa ne uimeasca cu imagini spectaculoase din univers. Cercetatorii au descoperit noi exoplanete care ar putea adaposti viata. Aceste descoperiri ne apropie tot mai mult de raspunsul la intrebarea: suntem singuri in univers?",
                Date = DateTime.Now.AddDays(-1),
                CategoryId = categories[1].Id,
                UserId = user.Id
            },
            new Article
            {
                Title = "Festivalul International de Film",
                Content = "Editia din acest an a festivalului a adus pe marile ecrane productii cinematografice exceptionale din intreaga lume. Regizori consacrati si talente emergente au prezentat opere care exploreaza conditia umana din perspective unice si captivante.",
                Date = DateTime.Now.AddDays(-2),
                CategoryId = categories[2].Id,
                UserId = user.Id
            },
            new Article
            {
                Title = "Romania la Campionatul European",
                Content = "Echipa nationala de fotbal a Romaniei a avut o prestatie remarcabila la ultimul turneu european. Jucatorii au demonstrat determinare si spirit de echipa, aducand bucurie milioanelor de suporteri romani.",
                Date = DateTime.Now.AddDays(-3),
                CategoryId = categories[3].Id,
                UserId = user.Id
            },
            new Article
            {
                Title = "Viitorul programarii web",
                Content = "Tehnologiile web evolueaza rapid. Framework-uri precum React, Vue si Angular domina piata, in timp ce WebAssembly promite performante native in browser. Dezvoltatorii trebuie sa se adapteze constant la noile tendinte pentru a ramane competitivi.",
                Date = DateTime.Now.AddDays(-4),
                CategoryId = categories[0].Id,
                UserId = user.Id
            }
        };

        context.Articles.AddRange(articles);
        await context.SaveChangesAsync();
        Console.WriteLine("Articles added.");

        Console.WriteLine("Seeding completed successfully!");
        Environment.Exit(0);
    }
}
