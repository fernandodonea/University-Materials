function drawTable(nrows, ncols) {
   let container=document.getElementById('container');
   let tabel=document.createElement('table');
   tabel.setAttribute('id','gridMare');

   for(let i=0;i<nrows;i++)
   {
      let rand=document.createElement("tr");
      for(let j=0;j<ncols;j++)
      {
         let celula=document.createElement("td");
         celula.classList.add('r'+i,'c'+j)
         celula.addEventListener('click',clickCellListener);
         rand.appendChild(celula);
      }
      tabel.appendChild(rand);
   }
   container.appendChild(tabel);
}

function clickCellListener(event) {
   let clasa=this.classList;
   let rand=clasa[0].slice(1);
   let coloana=clasa[1].slice(1);
   let cul=document.getElementById('colorPicker').value;
   drawPixel(rand,coloana,cul);
}



function colorCol(column, color) {
/*
   2. Colorați coloana 'column' din tabla de desenat cu culoarea 'color'.
*/
   let coloana=document.getElementsByClassName('c'+column);
   let n=coloana.length;
   for(let i=0;i<n;i++)
   {
      coloana[i].style.backgroundColor=color;
   } 
}

function colorRow(row, color) {
/*
   2. Colorați rândul 'row' din tabla de desenat cu culoarea 'color'.
*/
   let rand=document.getElementsByClassName("r"+row);
   let m=rand.length;

   for (let j=0;j<m;j++)
   {
      rand[j].style.backgroundColor=color;
   }

}

function rainbow(target) {
   let colors = ["rgb(255, 0, 0)", "rgb(255, 154, 0)", "rgb(240, 240, 0)", "rgb(79, 220, 74)", "rgb(63, 218, 216)", "rgb(47, 201, 226)", "rgb(28, 127, 238)", "rgb(95, 21, 242)", "rgb(186, 12, 248)", "rgb(251, 7, 217)"];
/*
   3. Desenați un curcubeu pe verticală sau orizontală conform argumentului 'target' folosind culorile din 'colors' și funcțiile 'colorCol' și 'colorRow'.     
*/
   if(target=='orizontal')
   {
      let k=-1;
      let n=document.getElementsByTagName("tr").length;
      for(let i=0;i<n;i++)
      {
         if(i%3==0)k=k+1;
         colorRow(i,colors[k]);
         k=k%10;
      }
      
   }
   else if(target=='vertical')
   {
      let k=-1;
      let m=document.getElementsByTagName('td').length
      for(let j=0;j<m;j++)
      {
         if(j%3==0)k=k+1;
         k=k%10;
         colorCol(j,colors[k]);
      }
      

   }
}
function curcubeu()
{
   let pos=['orizontal','vertical'];
   let x=Math.floor(Math.random()*2);
   rainbow(pos[x]);
}

function clearGrid() {
   let n=document.getElementsByTagName('tr').length;
   let m=document.getElementsByTagName('td').length/n;
   for(let i=0;i<n;i++)
   {
      drawLine(i,0,i,m-1,'white');
   }

}

function getNthChild(element, n) {
   return element.children[n];

};

function drawPixel(row, col, color) {	
/*
   5. Colorați celula de la linia 'row' și coloana 'col' cu culoarea `color'.
*/
   let rand = document.getElementsByClassName("r"+row);
   rand[col].style.backgroundColor=color;
}

function drawLine(r1, c1, r2, c2, color) {
/*
   6. Desenați o linie (orizontală sau verticală) de la celula aflată 
   pe linia 'r1', coloana 'c1' la celula de pe linia 'r2', coloana 'c2'
   folosind culoarea 'color'. 
   Hint: verificați mai întâi că punctele (r1, c1) și (r2, c2) definesc
   într-adevăr o linie paralelă cu una dintre axe.
*/
   if (r1==r2)
   {
      
      for(let j=c1;j<=c2;j++)
      {
         drawPixel(r1,j,color);
      }
   }
   else if(c1==c2)
   {
      for(let i=r1;i<=r2;i++)
      {
         drawPixel(i,c1,color);
      }
   }
}

function drawRect(r1, c1, r2, c2, color) {
/*
   7. Desenați, folosind culoarea 'color', un dreptunghi cu colțul din 
   stânga sus în celula de pe linia 'r1', coloana 'c1', și cu 
   colțul din dreapta jos în celula de pe linia 'r2', coloana 'c2'.
*/
   drawLine(r1,c1,r1,c2,color);
   drawLine(r2,c1,r2,c2,color);
   drawLine(r1,c1,r2,c1,color);
   drawLine(r1,c2,r2,c2,color);

   
}

function drawPixelExt(row, col, color) {
/*
   8. Colorați celula de la linia 'row' și coloana 'col' cu culoarea 'color'.
   Dacă celula nu există, extindeți tabla de desenat în mod corespunzător.
*/
   let tabel=document.getElementById('gridMare');
   let n=document.getElementsByTagName('tr').length;
   let m=document.getElementsByTagName('td').length/n;
   if (row>=n)
   {
      for(let i=n;i<=row;i++)
      {
         let rand=document.createElement("tr");
         for(let j=0;j<m;j++)
         {
            let celula=document.createElement("td");
            celula.classList.add('r'+i,'c'+j)
            rand.appendChild(celula);
         }
         tabel.appendChild(rand);
      }
   }
   n=document.getElementsByTagName('tr').length;
   if (col>=m){
      let tabel=document.getElementById('gridMare');
      for (let i=0;i<n;i++)
      {
      
         for(let j=m;j<=col;j++)
         {
            let celula=document.createElement("td");
            celula.classList.add('r'+i,'c'+j);
            tabel.rows[i].appendChild(celula);
           
         }
      }
   }
   drawPixel(row,col,color);
   
}
function colorMixer(colorA, colorB, amount){
   let cA = colorA * (1 - amount);
   let cB = colorB * (amount);
   return parseInt(cA + cB);
}

function drawPixelAmount(row, col, color, amount) {
   /* 
   9. Colorați celula la linia 'row' și coloana 'col' cu culoarea 'color'
   în funcție de ponderea 'amount' primită ca argument (valoare între 0 și 1). 
   Dacă 'amount' are valoarea:
   1, atunci celula va fi colorată cu 'color'
   0, atunci celula își va păstra culoarea inițială
   pentru orice altă valoare, culoarea inițială și cea dată de argumentul 
   'color' vor fi amestecate. De exemplu, dacă ponderea este 0.5, atunci 
   culoarea inițială și cea nouă vor fi amestecate în proporții egale (50%). 
   */

   /*   
   Hint 1: folosiți funcția colorMixer de mai sus.

   Hint 2: pentru un argument 'color' de forma 'rgb(x,y,z)' puteți folosi
   let newColorArray = color.match(/\d+/g); 
   pentru a obține un Array cu trei elemente, corespunzătoare valorilor
   asociate celor trei culori - newColorArray = [x, y, z]
   
   Hint 3: pentru a afla culoarea de fundal a unui element puteți folosi
   metoda getComputedStyle(element). Accesând proprietatea backgroundColor 
   a obiectului întors, veți obține un string de forma 'rgb(x,y,z)'.
   */
}

function delRow(row) {
/*
   10. Ștergeți linia cu numărul 'row' din tabla de desenat.
*/
}

function delCol(col) {
/*
   10. Ștergeți coloana cu numărul 'col' din tabla de desenat.
*/
}

function shiftRow(row, pos) {
/*
   11. Aplicați o permutare circulară la dreapta cu 'pos' poziții a
   elementelor de pe linia cu numărul 'row' din tabla de desenat. 
*/
}

function jumble() {
/*
   12. Folosiți funcția 'shiftRow' pentru a aplica o permutare circulară
   cu un număr aleator de poziții fiecărei linii din tabla de desenat.
*/
}

function transpose() {
/*
   13. Transformați tabla de desenat în transpusa ei.
*/
}

function flip(element) {
/*
   14. Inversați ordinea copiilor obiectului DOM 'element' primit ca argument.
*/
}

function mirror() {
/*
   15. Oglindiți pe orizontală tabla de desenat: luați jumătatea stângă a tablei, 
   aplicați-i o transformare flip și copiați-o în partea dreaptă a tablei.
*/
}

function smear(row, col, amount) {
/*
   16. Întindeți culoarea unei celule de pe linia 'row' și coloana 'col' în celulele
   învecinate la dreapta, conform ponderii date de 'amount' (valoare între 0 și 1).
   Cu colorarea fiecărei celule la dreapta, valoarea ponderii se înjumătățește. 
   Hint: folosiți funcția 'drawPixelAmount'.
*/
}



window.onload = function(){
    const rows = 50;
    const cols = 50;	
    
   drawTable(rows, cols);
   colorCol(4,'red');
   colorRow(1,'blue');
   rainbow('vertical');
   drawPixel(2,2,'black');
   drawLine(1,4,20,4,'black');
   drawRect(1,2,10,6,'pink');
   drawPixelExt(31,31,'black');


   let btn=document.getElementById('curcubeu');
   btn.addEventListener('click',curcubeu);

   let btn2=document.getElementById('sterge');
   btn2.addEventListener('click',clearGrid);

   

}


