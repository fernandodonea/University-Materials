



window.onload = function() {  
    
    let counter=document.createElement("div");
    counter.setAttribute("id","counter");
    counter.innerHTML="<p>0</p>";
    document.body.appendChild(counter);
    
    
    let container=document.createElement("div");
    container.setAttribute("id","container");
    document.body.appendChild(container);

    document.body.addEventListener("keydown",drawPunct);

    //slider
    let range=document.createElement("input");
    range.setAttribute("type","range");
    range.setAttribute("id","range");
    range.setAttribute("min","20");
    range.setAttribute("max","150");
    range.setAttribute("value","20");
    container.appendChild(range);
    

   


    function drawPunct(event){

        let container=document.getElementById("container");

        let culoare="";

        if(event.key=="r")
            culoare="red";
        else if(event.key=="g")
            culoare="green";
        else if(event.key=="y")
            culoare="yellow";
        else if(event.key=="b")
            culoare="blue";


        let punct=document.createElement("div");
        punct.style.borderRadius="50%";

        //dimensiune
        punct.style.width=document.getElementById("range").value+"px";
        punct.style.height=document.getElementById("range").value+"px";

        //culoare
        punct.style.backgroundColor=culoare;

        //pozitie
        punct.style.position = "absolute";
        let w = window.innerWidth;
        let h = window.innerHeight;
        let posx = Math.floor(Math.random() * w);
        let posy = Math.floor(Math.random() * h);
        punct.style.left = posx+"px";
        punct.style.top = posy+"px";

        //clonare
        punct.addEventListener("click",clonePunct)

        container.appendChild(punct);

        //Number() pentru ca pe localsotrage se salveaza doar stringuri
        let x=Number(localStorage.getItem("counter"));
        if (x)
            {
                localStorage.setItem("counter",x+1);
            }
        else
            {
                localStorage.setItem("counter",1);
            }
        paragraf=document.createElement("p");
        paragraf.innerHTML=localStorage.getItem("counter");
        document.getElementById("counter").innerHTML="";
        document.getElementById("counter").appendChild(paragraf);

    
        
    }

    function clonePunct(event)
    {
        let container=document.getElementById("container");

        let punct=document.createElement("div");
        punct.style.borderRadius="50%";

        //dimensiune
        punct.style.width=event.target.style.width;
        punct.style.height=event.target.style.height;

        //culoare
        punct.style.backgroundColor=event.target.style.backgroundColor;

        //pozitie
        punct.style.position = "absolute";
        let w = window.innerWidth;
        let h = window.innerHeight;
        let posx = Math.floor(Math.random() * w);
        let posy = Math.floor(Math.random() * h);
        punct.style.left = posx+"px";
        punct.style.top = posy+"px";

        //clonare
        punct.addEventListener("click",clonePunct)

        container.appendChild(punct);
        


        let x=Number(localStorage.getItem("counter"));
        if (x)
            {
                localStorage.setItem("counter",x+1);
            }
        else
            {
                localStorage.setItem("counter",1);
            }
        paragraf=document.createElement("p");
        paragraf.innerHTML=localStorage.getItem("counter");
        document.getElementById("counter").innerHTML="";
        document.getElementById("counter").appendChild(paragraf);

    }




     
 }