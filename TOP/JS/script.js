// console.log(2+2*2)
// let int = 1       // let создание переменной
// let str = "1"
// let bool = true || false
// let massiv = [1,2,3,4,5,6]
// let obj = {
//     "name" : "name",
//     "age" : 22,
// }

// class Auto{
//     constructor(name,age){  // __init__
//         this.name = name;
//         this.age = age;
//     }
//     changeName(){
//         console.log(this.name)
//     }
// }

// class AutoV2 extends Auto{
//     constructor(name,age){
//         this.name = name;
//         this.age = age;
//     }
// }

// function sum(a,b){
//     return a + b
// }

// let sum2 = (a,b) => {
//     return a + b
// }

// console.log(sum(2,3))
// // alert("работает")
// let x = prompt("Введите ваше имя"); // строка
// let y = +prompt("Введите только число"); // число +
// console.log(x,y)


// let i = 0;

// while(i < 10){
//     i++;
//     console.log(i)
// }

// for(let i = 0; i < 10; i++){
//     console.log(i)
// }

// let z = 1;
// let k = 2;

// if(z < k){
//     console.log("z < k")
// }
// else if(k < z){
//     console.log("k < z")
// }
// else if(k == z){
//     console.log("k = z")
// }

// else{
//     console.log("Ошибка")
// }

// Задание 1

// let x = +prompt("Введите первое число:");
// let y = +prompt("Введите второе число");
// let z = +prompt("Введите третье число");

// let sum = x + y + z;
// let proizv = x * y * z;

// console.log(`Сумма чисел: ${sum}`);
// console.log(`Произведение чисел: ${proizv}`);

// Задание 2

// let x = +prompt("Введите первое число - зарплата за месяц (руб.): ");
// let y = +prompt("Введите второе число - сумма месячного платежа по кредиту (руб.): ");
// let z = +prompt("Введите третье число - задолженность за коммунальные услуги (руб.): ");
// let ost = x - y - z;
// console.log(`Остаток после всех выплат - ${ost}руб.`);


// Задание 3

// let x = +prompt("Введите первое число: ");
// let y = +prompt("Введите второе число: ");
// let z = +prompt("Введите третье число: ");
// let vybor = +prompt("Выберите выводить сумму чисел (цифра 1) или произведение чисел (цифра 2):")

// if(vybor == 1){
//     console.log(`Сумма чисел -  ${x + y + z}`)
// }

// else{
//         console.log(`Произведение чисел - ${x * y * z}`)
//      }

// // Задание 4

// let x = +prompt("Введите первое число: ");
// let y = +prompt("Введите второе число: ");
// let z = +prompt("Введите третье число: ");
// let vybor = +prompt("Выберите выводить максимум из чисел (цифра 1), минимум из чисел (цифра 2), среднеарифметическое чисел (цифра 3):");
// let mn = Math.min(x,y,z);
// let mx = Math.max(x,y,z);
// let sr = (x + y + z)/3;

// if(vybor == 1){
//     console.log(`Максимум чисел -  ${mx}`)
// }
// else if(vybor == 2){
//     console.log(`Минимум чисел -  ${mn}`)
// }
// else{
    //  console.log(`Среднее арифметическое чисел - ${sr}`)
// }


// Задание 5

// let x = +prompt("Введите количество метров: ");
// let y = +prompt("Выберите действие (перевести в мили - 1, перевести в дюймы - 2, перевести в ярды - 3): ");
// if (y == 1){
//     console.log("Количество миль:");
//     console.log(x * 0.00062);
// }
// else if (y == 2){
//     console.log("Количество дюймов:");
//     console.log(x * 39.37);
// }
// else if (y == 3){
//     console.log("Количество ярдов:")
//     console.log(x * 1.09)
// }
// else{
//     console.log("Не верно выбранное действие!")
// }

// or ||
// and $$

// Задание 6

// let x = +prompt("Введите ваш возраст: ");
// if (x >= 0 && x < 12){
//     console.log("Вы ребенок");
// }
// else if (x >= 12 && x < 18){
//     console.log("Вы подросток");
// }
// else if (x >= 18 && x < 60){
//     console.log("Вы взрослый");
// }
// else{
//     console.log("Вы пенсионер");
// }

// Задание 7

// let x = +prompt("Введите число 0 до 9: ");
// if (x == 1){
//     console.log("1 - !");
// }
// else if (x == 2){
//     console.log("2 - @");
// }
// else if (x == 3){
//     console.log("3 - #");
// }
// else if (x == 4){
//     console.log("4 - $");
// }
// else if (x == 5){
//     console.log("5 - %");
// }
// else if (x == 6){
//     console.log("6 - ^");
// }
// else if (x == 7){
//     console.log("7 - &");
// }
// else if (x == 8){
//     console.log("8 - *");
// }
// else if (x == 9){
//     console.log("9 - (");
// }
// else{
//     console.log("0 - )");
// }

// Задание 8 

// let x = +prompt("Введите трехзначное число: ")
// x1 = x % 10;
// x2 = Math.floor(x/10);
// x3 = x2 % 10;
// x4 = Math.floor(x2/10);
// if (x1 != x3 && x1 != x4 && x3 != x4){
//     console.log("Одинаковых цифр нет");
// }
// else{
//     console.log("Одинаковые цифры есть");
// }

// Задание 9

let x = +prompt("Введите год: ");
if x % 4 != 0:
    print("Год обычный")
elif x % 4 == 0:
    if x % 100 != 0:
        print("Год високосный")
    elif x % 100 == 0:
        if x % 400 == 0:
            print("Год високосный")
        else:
            print("Год обычный")
    else:
        print()
else:
    print()