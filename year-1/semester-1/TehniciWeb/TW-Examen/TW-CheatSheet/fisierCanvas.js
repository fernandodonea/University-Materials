
window.onload = function() {
   
  

   const canvas=document.getElementById("canvasID");

   /*
         DREPTUNGHI

         fillRect(x, y, width, height)
            // desenează un dreptunghi plin

         strokeRect(x, y, width, height)
            // desenează un contur de dreptunghi

         clearRect(x, y, width, height)
            // șterge zona dreptunghiulară, făcând-o transparentă

   */


   /*
         PATH

            1. ctx.beginPath();

            2. ctx.moveTo(x,y);

            3. ctx.lineTo(25,220);
               ctx.lineTo(110,240);
               ctx.lineTo(110,10);

            4. ctx.fill(); sau ctx.stroke();

            5. ctx.closePath();


   */



  
   /*
            CERCURI

            arc(x, y, radius, startAngle, endAngle, counterclockwise)

            // arc centrat în (x, y) cu raza r 
            //  începând de la startAngle și până la endAngle, 
            // în direcția dată de counterclockwise 
    */

   
   draw();
   
             
   function draw() {
        const canvas=document.getElementById("canvasID");
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
             
  }   
        
       
      
