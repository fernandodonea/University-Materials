function infoAlbum(i){
   let url="albums/"+i+".json";
   var promiseFetch = fetch(url);
   var album;

   promiseFetch.then((response) => {
      if (!response.ok) {
         throw new Error(`HTTP error: ${response.status}`);
      }
      return response.text();
        })
        
        .then(function(text) {   
         album = JSON.parse(text); 
     
         ////aici incepem sa prelucram datele din json 
         let album_name=album.name;
         let album_artist=album.artist;
         let album_year=album.year;
         let album_label=album.label;
         let album_genre=album.genres;
           
         
         let container=document.getElementById("info");
         container.innerHTML="";

         let nume=document.createElement('h2');
         nume.innerHTML=album_name;

         let artist=document.createElement('p');
         artist.innerHTML="Artist: "+album_artist;

         let year=document.createElement('p');
         year.innerHTML="Year: "+album_year;

         let label=document.createElement('p');
         label.innerHTML="Label: "+album_label;

         let genre=document.createElement('p');
         genre.innerHTML="Genres: ";
         let n=album_genre.length;
         for(let i=0;i<n;i++)
         {
            genre.innerHTML+=album_genre[i];
            if(i<n-1)
            genre.innerHTML+=", ";
         }

         container.appendChild(nume);
         container.appendChild(artist);
         container.appendChild(year);
         container.appendChild(label);
         container.appendChild(genre);

           
        
        })
           .catch(function(err){
        alert(err);});   

   

}

function cerereAlbum(){
   let url = 'albums.json';    
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
      let container=document.getElementById("gallery");
     
      for(let i=0;i<n;i++)
      {
         let x=possanswers[i].image;
         let imagine=document.createElement('img');
         imagine.style.width="200px";
         imagine.style.height="200px";
         imagine.setAttribute("src","/images/"+x);
         imagine.setAttribute("alt","imagine album");
         container.appendChild(imagine);
         imagine.addEventListener("click",function(){infoAlbum(i);});
      }
   
   })
      .catch(function(err){
   alert(err);}); 
}

window.onload = function() {  
   cerereAlbum();
    
}