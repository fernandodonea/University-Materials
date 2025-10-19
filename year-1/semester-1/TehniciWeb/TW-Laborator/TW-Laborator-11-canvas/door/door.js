
window.onload = function() {
   
   let doorColor='red';

   const canvas=document.getElementById("canvdoor");
   canvas.addEventListener("click",colorBlack);
   

   
   draw();
   
             
   function draw() {
        const canvas=document.getElementById("canvdoor");
        if(canvas.getContext) {
            const ctx=canvas.getContext("2d");

            //desenam frame-ul usii
            ctx.strokeStyle='red';
            ctx.lineWidth=5;
            ctx.strokeRect(20,20,120,200);
            //stergem partea de jos
            ctx.clearRect(23,215,114,20);

   
            
             //desenam usa
            ctx.beginPath();
            //punctul din care incepem
            ctx.moveTo(25,30);
            //definim forma usii
            ctx.lineTo(25,220);
            ctx.lineTo(110,240);
            ctx.lineTo(110,10);
            ctx.fillStyle=doorColor;
            ctx.fill();
            ctx.strokeStyle='white';
            ctx.lineWidth='5'
            ctx.stroke();
            ctx.closePath();

            //desenam clanta
            ctx.beginPath();
            ctx.arc(100,120,5,0,360);
            ctx.fillStyle='white';
            ctx.fill();
            ctx.closePath;
        }
 
   }          
             
   function colorBlack() {
      // colorăm ușa în negru    
      if(doorColor=='red')
         doorColor='black';
      else
         doorColor='red';
      draw();
   
   }
}   
        
       
      
