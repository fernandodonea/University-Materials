function cerereJSON(){
   let url = 'numeFisier.json';    
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
     
     
      for(let i=0;i<n;i++)
      {
         let x=possanswers[i].tag;
         let imagine=document.createElement('tag');

      }
   
   })
      .catch(function(err){
   alert(err);}); 
}

window.onload = function() {  
   cerereJSON();
    
}