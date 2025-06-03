function appearBadger()
{
    let badger=document.createElement('img');
    badger.setAttribute('src','resources/images/badger-1.png');

    badger.style.position='absolute';
    badger.style.left=Math.random()*window.innerWidth+'px';
    badger.style.top=Math.random()*window.innerHeight+'px';

    badger.addEventListener('click',danseazaBadger);

    document.body.appendChild(badger);

}

function appearCiuperca()
{
    let ciupe=document.createElement('img');
    ciupe.setAttribute('src','resources/images/mush.png');

    ciupe.style.position='absolute';
    ciupe.style.left=Math.random()*window.innerWidth+'px';
    ciupe.style.top=Math.random()*window.innerHeight+'px';

    document.body.appendChild(ciupe);

}
function danseazaBadger(event) {
    let badger = event.target;

    if (badger.dataset.dancing === 'true') {
        badger.dataset.dancing = 'false';
        badger.remove();
        return;
    }

    badger.dataset.dancing = 'true';
    let pozitiiDans = [
        'resources/images/badger-2.png',
        'resources/images/badger-3.png',
        'resources/images/badger-4.png',
        'resources/images/badger-1.png'
    ];
    let index = 0;

    function schimbaPozitia() {
        if (badger.dataset.dancing !== 'true') return;
        badger.setAttribute('src', pozitiiDans[index]);
        index = (index + 1) % pozitiiDans.length;
        setTimeout(schimbaPozitia, 200);

        if (index== 3)
        {
            var x=Number(localStorage.getItem('genoflexiuni'));
            if (!x)
            {
                localStorage.setItem('genoflexiuni',1);
                let paragraf=document.getElementById('geno');
                paragraf.innerText='Genoflexiuni: 1';
            }
            else{
                localStorage.setItem('genoflexiuni',x+1);
                let paragraf=document.getElementById('geno');
                paragraf.innerText='Genoflexiuni: '+(x);

                if(x%5==0)
                {
                    appearCiuperca();
                }
                
            }

        }
       
    }
    schimbaPozitia();
}


var played=false;
let sunet=document.createElement('audio');
sunet.setAttribute('src','resources/badger.mp3');
function playMusic()
{

    
    if (played==false)
    {
        sunet.play();
        played=true;
    }
    else
    {
        sunet.pause();
        played=false;
    }

}


function taste(event)
{
    if(event.key=='b')
    {
        appearBadger();
    }
    else if(event.key=='p')
    {
        playMusic();
    }

}


window.onload=function(){
    document.addEventListener('keypress',taste);

    let paragraf=document.createElement('p');
    paragraf.setAttribute('id','geno');
    paragraf.innerText='Genoflexiuni: 0';
    document.body.appendChild(paragraf);

    

}