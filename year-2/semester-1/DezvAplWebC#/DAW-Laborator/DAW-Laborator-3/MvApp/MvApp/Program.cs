var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllersWithViews();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Home/Error");
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseRouting();

app.UseAuthorization();

app.MapStaticAssets();


///TODO
/// 


// /concatenare/ab/cf
app.MapControllerRoute(
    name: "Concatenare",
    pattern: "/concatenare/{s1?}/{s2?}",
    defaults: new
    {
        controller = "Examples",
        action = "Concatenare" 
    }
    )
    .WithStaticAssets();


// /produs/param1/param2
app.MapControllerRoute(
    name: "Produs",
    pattern: "produs/{a}/{b?}",
    defaults: new { controller = "Examples", action = "Produs" }
);


//ex 1.3

// /operatie/param1/param2/op
app.MapControllerRoute(
    name: "Operatie",
    pattern: "/operatie/{param1?}/{param2?}/{op?}",
    defaults: new { controller = "Examples", action = "Operatie" }
    )
    .WithStaticAssets();


// /Student/Index

//varianta 1
app.MapControllerRoute(
    name: "StudentsIndex",
    pattern: "{contoller=Students}/{actions=Index}")
    .WithStaticAssets();


//varianta2
app.MapControllerRoute(
    name: "StudentsAll",
    pattern: "students/all",

defaults: new {controller="Students",action="Index"})
    .WithStaticAssets();


// /students/new
app.MapControllerRoute(
    name: "StudentsCreate",
    pattern: "students/new",
    defaults: new { controller = "Students", action = "Create" }
);




// /students/show/{id}
app.MapControllerRoute(
    name: "StudentsCreate",
    pattern: "students/show/{id?}",
    defaults: new { controller = "Students", action = "Show" }
);


// /students/edit/{id}
app.MapControllerRoute(
    name: "StudentsCreate",
    pattern: "students/edit/{id?}",
    defaults: new { controller = "Students", action = "Edit" }
);




/// RUTA DEFAULT

app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Index}/{id?}")
    .WithStaticAssets();



app.Run();
