function cerereJSON(){
    let url = 'fibacup.json';    
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

       let container=document.getElementById('container');
       container.innerHTML="";
 
       ////aici incepem sa prelucram datele din json 
       let n=possanswers.length;
       let x=Math.floor(Math.random()*n);
       let echipa1=possanswers[x].home;
       let steag1=possanswers[x].homeflag;
       let echipa2=possanswers[x].guest;
       let steag2=possanswers[x].guestflag;

       let data=possanswers[x].date;
       let ora=possanswers[x].time;

       
       let imagine1=document.createElement("img");
       imagine1.setAttribute('src',"resources/"+steag1);
       
       //functie pentru a afisa numele echipei home la hover
       imagine1.addEventListener('mouseover',function()
       {
        let detaliu=document.createElement('p');
        detaliu.setAttribute('id','detaliu1');
        detaliu.innerHTML=echipa1;
        container.appendChild(detaliu);

        //functie pentru a sterge detaliile la hover out
       });
       imagine1.addEventListener('mouseout',function()
       {
        let detaliu=document.getElementById('detaliu1');
        container.removeChild(detaliu);
       });
       container.appendChild(imagine1);




       let imagine2=document.createElement("img");
       imagine2.setAttribute('src',"resources/"+steag2);
        //functie pentru a afisa numele echipei home la hover
        imagine2.addEventListener('mouseover',function()
        {
         let detaliu=document.createElement('p');
         detaliu.setAttribute('id','detaliu2');
         detaliu.innerHTML=echipa2;
         container.appendChild(detaliu);
 
         //functie pentru a sterge detaliile la hover out
        });
        imagine2.addEventListener('mouseout',function()
        {
         let detaliu=document.getElementById('detaliu2');
         container.removeChild(detaliu);
        });
       container.appendChild(imagine2);



       let paragraf=document.createElement("p");
       paragraf.innerHTML=data+" at "+ora;
       container.appendChild(paragraf);





    
    })
       .catch(function(err){
    alert(err);}); 
 }
 
 window.onload = function() {  
    cerereJSON();
     
 }



window.onload = function() {
   
    const canvas=document.getElementById("court");
    canvas.addEventListener('click',cerereJSON);
    draw();
         
    function draw() {
         const canvas=document.getElementById("court");
         if(canvas.getContext) {
             const ctx=canvas.getContext("2d");
 
             //desenam court-ul 
            ctx.fillStyle='coral';
            ctx.fillRect(20,20,400,200);

             //desenam linia din mijloc
            ctx.beginPath();
            ctx.moveTo(220,20);
            ctx.lineTo(220,220);
            ctx.strokeStyle='white';
            ctx.lineWidth=5;
            ctx.stroke();
            ctx.closePath();

            //desenam cercul din mijloc
            ctx.beginPath()
            ctx.arc(220,120,30,0,360);
            ctx.strokeStyle='white';
            ctx.stroke();
            ctx.closePath;

            //teren echipa1
            ctx.beginPath()
            ctx.arc(20,120,90,0,360);
            ctx.strokeStyle='white';
            ctx.stroke();
            ctx.closePath();

            ctx.strokeStyle='white'
            ctx.strokeRect(20,100,40,40);

            ctx.beginPath()
            ctx.arc(60,120,20,0,360);
            ctx.strokeStyle='white';
            ctx.stroke();
            ctx.closePath;





            ////teren echipa2
            ctx.beginPath()
            ctx.arc(420,120,90,0,360);
            ctx.strokeStyle='white';
            ctx.stroke();
            ctx.closePath();

            ctx.strokeStyle='white'
            ctx.strokeRect(380,100,40,40);

            ctx.beginPath()
            ctx.arc(380,120,20,0,360);
            ctx.strokeStyle='white';
            ctx.stroke();
            ctx.closePath;



             
 
    
            
         }
  
    }          
              
   }   
         
        
       
 