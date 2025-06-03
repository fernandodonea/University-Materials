function appearBubble()
{
    let bub=document.createElement('img');
    bub.setAttribute('src','resources/images/bubble-1.png');
    bub.setAttribute('class','bubble');


    bub.style.position='absolute';
    bub.style.left=Math.random()*window.innerWidth+'px';
    bub.style.top=Math.random()*window.innerHeight+'px';

    bub.addEventListener('click',spargeBubble);


    document.body.appendChild(bub);
}




function spargeBubble(event) {
    let bub = event.target;


    let stagii = [
        'resources/images/bubble-2.png',
        'resources/images/bubble-3.png',
        'resources/images/bubble-4.png',

    ];
    
    let i=0;
    for(i = 0; i < stagii.length; i++)
    {
            setTimeout(schimba, 500*(i+1), i);
            function schimba(i) {
                bub.setAttribute('src',stagii[i])
            }
    }

    
    var x=Number(localStorage.getItem('spart'));
            if (!x)
            {
                localStorage.setItem('spart',1);
                let paragraf=document.getElementById('sparteTotal');
                paragraf.innerText='Bule sparte: 1';
            }
            else{
                localStorage.setItem('spart',x+1);
                let paragraf=document.getElementById('sparteTotal');
                paragraf.innerText='Bule sparte: '+(x);

                if(x%5==0)
                {
                    appearCiuperca();
                }
                
            }

    setTimeout(function() {
        bub.remove();
    }, 500*(i+1));

}
function danseazaBubble()
{
    let bule=document.getElementsByClassName("bubble");
    let n=bule.length;
    for(let i=0;i<n;i++)
    {
        deplasare(bula[i]);

    }
}


let intervalId;

function deplasare(bula) {
    let x = Math.random() * window.innerWidth;
    let y = Math.random() * window.innerHeight;

    bula.style.left = x + 'px';
    bula.style.top = y + 'px';

}

function danseazaBubble() {
    let bule = document.getElementsByClassName("bubble");
    let n = bule.length;
    intervalId = setInterval(() => {
        for (let i = 0; i < n; i++) {
            deplasare(bule[i]);
        }
    }, 1000);
}

function stopdanseazaBubble() {
    clearInterval(intervalId);
}

function taste(event) {
    if (event.key == 's') {
        appearBubble();
    }
    if (event.key == 'p') {
        danseazaBubble();
    }
    if (event.key == 'f') {
        stopdanseazaBubble();
    }
}




window.onload=function(){
    document.addEventListener('keypress',taste)
    
    let paragraf=document.createElement('p');
    paragraf.style.textAlign="right";
    paragraf.setAttribute('id','sparteTotal');
    paragraf.innerText='Bule sparte: 0';
    paragraf.style.color='white';
    document.body.appendChild(paragraf);

    
}

