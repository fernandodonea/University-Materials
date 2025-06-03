function drawMagic(culoare) {
    const canvas=document.getElementById("bila");
         if(canvas.getContext) {
             const ctx=canvas.getContext("2d");

             ctx.beginPath();
             ctx.arc(100,100,80,0,360);
             ctx.fillStyle='black';
             ctx.fill();
             ctx.closePath;

             ctx.beginPath();
             ctx.arc(100,100,40,0,360);
             ctx.fillStyle=culoare;
             ctx.fill();
             ctx.closePath;
         }

}
function draw() {
    const canvas=document.getElementById("bila");
    if(canvas.getContext) {
        const ctx=canvas.getContext("2d");

        ctx.beginPath();
        ctx.arc(100,100,80,0,360);
        ctx.fillStyle='black';
        ctx.fill();
        ctx.closePath;

        ctx.beginPath();
        ctx.arc(100,100,40,0,360);
        ctx.fillStyle='white';
        ctx.fill();
        ctx.closePath;

        ctx.font="50px Arial";
       ctx.fillStyle='black';
       ctx.fillText("8", 90, 120);
    }
}
function cerereJSON(varianta,culoare)
{
    let url = 'magic.json';    
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
       let rasp=[]
       let k=0;
       for(let i=0;i<n;i++)
       {
            if(possanswers[i].bool==varianta)
            {
                rasp[k]=possanswers[i].text;
                k++;
            }
       }
        let x=Math.floor(Math.random()*k);
        let mesaj=rasp[x];
        let paragraf=document.getElementById("mesaj");
        paragraf.style.color=culoare;
        paragraf.innerHTML=mesaj;
      

    
    })
       .catch(function(err){
    alert(err);}); 
}



window.onload=function(){

   
    draw();
    const canvas=document.getElementById("bila");      
    canvas.addEventListener('click',function(){
        let x=Math.floor(Math.random()*3);
        let culori=['red','green','yellow'];
        let variante=['no','yes','maybe'];
        drawMagic(culori[x]);
        cerereJSON(variante[x],culori[x]);
        
    });


}