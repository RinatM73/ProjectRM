let a = document.querySelector('#a');
let b = document.querySelector('#b');
let c = document.querySelector('#c');

let otvetD = document.querySelector('#otvetD');
let otvetx1 = document.querySelector('#otvetx1');
let otvetx2 = document.querySelector('#otvetx2');

let resh = document.querySelector('#resh');

function D(){
    otvetD.innerHTML = Number(b.value)**2 - 4*Number(a.value)*Number(c.value)
}

function x1(){
    otvetx1.innerHTML = (Number(-b.value) + Math.sqrt(otvetD.innerHTML))/2*Number(a.value)
}

function x2(){
    otvetx2.innerHTML = (Number(-b.value) - Math.sqrt(otvetD.innerHTML))/2*Number(a.value)
}

resh.addEventListener("click", D);
resh.addEventListener("click", x1);
resh.addEventListener("click", x2);

let body = document.body;