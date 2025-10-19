
var nume = prompt("Hai să jucam X si 0. Cum te cheama?");
var simbol = prompt("Bună, "+nume+" . Cu ce vrei să joci? X sau 0? X începe primul.")

var v= new Array();
for (let i=0;i<=8;i++)
	v[i]="?";
//sau var v=Array(9).fill("?");

function getBoardString()
{
	let board="";
	for(let i=0;i<3;i++)
	{
		let linie="| ";
		for(let j=0;j<3;j++)
		{
			if(v[i*3+j]=="?")
				linie+=i*3+j+1+" | ";
			else linie+=v[i*3+j]+" | ";

		}
		board+=linie+"\n";
	}
	return board;
}
function printt(s)
{
	prompt(getBoardString(s)+"\n"+ "your next move");
}

function mutare() {
	x=prompt(printt(v)+'\n'+"Unde vrei să pui următorul semn?")


}
mutare();


