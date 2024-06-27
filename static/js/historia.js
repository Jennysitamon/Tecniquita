const historiaImg = document.getElementById('historia-img');
const imagenes = [
    '/static/img/historia1.png',
    '/static/img/historia2.png'
];
let indice = 0;
let primeraCarga = true;

function cambiarImagen() {
    if (primeraCarga) {
        historiaImg.src = imagenes[indice]; 
        primeraCarga = false;
    } else {
        historiaImg.style.opacity = 0; 
        setTimeout(() => {
            historiaImg.src = imagenes[indice]; 
            historiaImg.style.opacity = 1; 
        }, 200); 
    }
    indice = (indice + 1) % imagenes.length;
}

setInterval(cambiarImagen, 2000); 
