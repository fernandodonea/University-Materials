function cerereJSON(){
    let url = 'zap.json';    
    var promiseFetch = fetch(url);
    var possanswers;
    
    promiseFetch.then((response) => {
  if (!response.ok) {
     throw new Error(`HTTP error: ${response.status}`);
  }
  return response.text();
    })
    
    .then(function(text) {   
       possanswers = JSON.parse(text); 
 
       ////aici incepem sa prelucram datele din json 
       let n=possanswers.length;
       let x=Math.floor(Math.random()*n);
       let film_titlu=possanswers[x].title;
       let film_data=possanswers[x].date;
       let film_ora=possanswers[x].time;
       let film_poster=possanswers[x].poster;
       let film_personaje=possanswers[x].starring;
       let film_scor=possanswers[x].rate;
       

       let container=document.getElementById('container');
       container.innerHTML="";

       let titlu=document.createElement('h2');
       titlu.innerHTML=film_data;
       container.appendChild(titlu);

       let subtitlu=document.createElement('p');
       subtitlu.innerHTML=film_ora+" "+film_titlu;
       container.appendChild(subtitlu);

       let imagine=document.createElement("img");
       imagine.setAttribute('src',"resources/"+film_poster);

       //functie pentru a afisa detaliile filmului la hover
       imagine.addEventListener('mouseover',function()
       {
        let detaliu=document.createElement('p');
        detaliu.setAttribute('id','detaliu');
        detaliu.innerHTML="Cu: "+film_personaje+" rating: "+film_scor;
        container.appendChild(detaliu);

        //functie pentru a sterge detaliile filmului la hover out
       });
       imagine.addEventListener('mouseout',function()
       {
        let detaliu=document.getElementById('detaliu');
        container.removeChild(detaliu);
       });
       container.appendChild(imagine);
       


      
      
      
    
    })
       .catch(function(err){
    alert(err);}); 
 }
 


window.onload = function() {

    const canvas=document.getElementById("tv");
    canvas.addEventListener('click',cerereJSON);

    draw();
                
   function draw() {
    const canvas=document.getElementById("tv");
        if(canvas.getContext) {
            const ctx=canvas.getContext("2d");
        
            ctx.fillStyle='gray';
            ctx.fillRect(20,20,270,180);

            //ecran
            ctx.fillStyle='white';
            ctx.fillRect(35,35,220,140);

            ctx.beginPath();
            ctx.arc(270,70,10,0,360);
            ctx.fillStyle='white';
            ctx.fill();
            ctx.closePath;

            ctx.beginPath();
            ctx.arc(270,100,8,0,360);
            ctx.fillStyle='white';
            ctx.fill();
            ctx.closePath;

            ctx.beginPath();
            ctx.arc(270,130,6,0,360);
            ctx.fillStyle='white';
            ctx.fill();
            ctx.closePath;


            ctx.fillStyle='white';
            ctx.fillRect(40,40,30,130);
            ctx.fillStyle='yellow';
            ctx.fillRect(70,40,30,130);
            ctx.fillStyle='green';
            ctx.fillRect(100,40,30,130);
            ctx.fillStyle='lightblue';
            ctx.fillRect(130,40,30,130);
            ctx.fillStyle='magenta';
            ctx.fillRect(160,40,30,130);
            ctx.fillStyle='red';
            ctx.fillRect(190,40,30,130);
            ctx.fillStyle='blue';
            ctx.fillRect(220,40,30,130);
        }
    }
    
}