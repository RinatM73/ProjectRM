// let plus1 = document.getElementById("plus");
let plus = document.querySelector("#plus");
let minus = document.querySelector("#minus");
let out = document.querySelector("#out")
console.log(plus);
console.log(minus);
console.log(out);

// let head = document.querySelector("head");
// console.log(head);


let h1 = document.querySelector("#h1");
h1.innerHTML = "УРОК" + 4;

let title = document.querySelector("title");
title.innerHTML = "UROK" + 5;

let i = 0;

function plusOut(){
    i++;
    out.innerHTML = i;
}

function minusOut(){
    i--;
    out.innerHTML = i;
}

plus.addEventListener("click",plusOut);
minus.addEventListener("click",minusOut);

let number1 = document.querySelector("#number1");
let number2 = document.querySelector("#number2");

let calcPlus = document.querySelector("#calcPlus");
let calcMinus = document.querySelector("#calcMinus");
let calcMul = document.querySelector("#calcMul");
let calcDiv = document.querySelector("#calcDiv");

let otvet = document.querySelector("#otvet");
// let ffff = "123";
// ffff = Number(ffff)

function fPlus(){
    otvet.innerHTML = Number(number1.value) + Number(number2.value);
}

function fMinus(){
    otvet.innerHTML = Number(number1.value) - Number(number2.value);
}

function fMul(){
    otvet.innerHTML = Number(number1.value) * Number(number2.value);
}

function fDiv(){
    otvet.innerHTML = Number(number1.value) / Number(number2.value);
}

calcPlus.addEventListener("click", fPlus);
calcMinus.addEventListener("click", fMinus);
calcMul.addEventListener("click", fMul);
calcDiv.addEventListener("click", fDiv);

let body = document.body;
