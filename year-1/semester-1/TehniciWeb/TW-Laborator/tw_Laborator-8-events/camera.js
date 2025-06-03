




window.onload = function(){
    const img = document.querySelector('#vizor img');
    const vizor = document.getElementById('vizor');
    const step = 10; // Pasul de deplasare în pixeli
    let plus=0.2;
    let minus=0.2;

    window.addEventListener('keydown', function(event) {
        const style = window.getComputedStyle(img);
        let marginLeft = parseInt(style.marginLeft) || 0;
        let marginTop = parseInt(style.marginTop) || 0;

        switch (event.key) {
            case 'w':
                if (marginTop < 0) {
                    img.style.marginTop = (marginTop + step) + 'px';
                }
                break;
            case 's':
                if (vizor.clientHeight - marginTop < img.clientHeight) {
                    img.style.marginTop = (marginTop - step) + 'px';
                }
                break;
            case 'a':
                if (marginLeft < 0) {
                    img.style.marginLeft = (marginLeft + step) + 'px';
                }
                break;
            case 'd':
                if (vizor.clientWidth - marginLeft < img.clientWidth) {
                    img.style.marginLeft = (marginLeft - step) + 'px';
                }
                break;
            case "+":
                img.style.transform = `scale(${1 + plus})`;
                plus += 0.1;
                minus -= 0.1;
                break;
            case "-":
                img.style.transform = `scale(${1 + minus})`;
                minus -= 0.1;
                plus+=0.1;
                break;
        }
    });
}


