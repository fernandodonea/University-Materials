function incarcaXML()
{
	fetch("cinemateca.xml").then(response => {
		return response.text();
		}).then(xmlString => {
		const xmlDocument = new DOMParser().parseFromString(xmlString,"text/xml");
		const filme = xmlDocument.querySelectorAll("film");

		for(let film of filme) {
			let myDiv = document.createElement("div");

			let lista = document.createElement("ul");
			let titlu = document.createElement("h3");
			
			for(let x of film.children) {
				let listItem = document.createElement("li");
				if(x.tagName=='titlu')
				{
					titlu.textContent = x.textContent;
					myDiv.appendChild(titlu);
				}
				else
				{
					listItem.textContent = x.tagName + ": " + x.textContent;
					lista.appendChild(listItem);
				}
			}

			myDiv.appendChild(lista);
    
            
            document.body.appendChild(myDiv);
}	

});
}	



window.onload = function() {
	incarcaXML();
}