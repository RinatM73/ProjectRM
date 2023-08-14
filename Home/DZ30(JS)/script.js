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
// let x1 = x % 10;
// let x2 = Math.floor(x/10);
// let x3 = x2 % 10;
// let x4 = Math.floor(x2/10);
// if (x1 != x3 && x1 != x4 && x3 != x4){
//     console.log("Одинаковых цифр нет");
// }
// else{
//     console.log("Одинаковые цифры есть");
// }

// Задание 9

// let x = +prompt("Введите год: ");
// if (x % 4 != 0){
//     console.log("Год обычный")
// }
// else if (x % 4 == 0){
//     if (x % 100 != 0){
//         console.log("Год високосный")
//     }  
//     else if (x % 100 == 0){
//         if (x % 400 == 0){
//             console.log("Год високосный")
//         }    
//         else{
//             console.log("Год обычный")
//         }      
//     }    
//     else{
//         console.log()
//     }    
// }
// else{
//     console.log()
// }
    
// Задание 10

// let x = +prompt("Введите пятиразрядное число: ");
// let x1 = x % 10;
// let x2 = Math.floor(x/10);
// let x3 = x2 % 10;
// let x4 = Math.floor(x2/10);
// let x5 = x4 % 10;
// let x6 = Math.floor(x4/10)
// let x7 = x6 % 10
// let x8 = Math.floor(x6/10)
// if (x1 == x8 && x3 == x7){
//     console.log("Число палиндром")
// }
    
// else{
//     console.log("Число не палиндром")
// }

// Задание 11

// let x = +prompt("Введите количество долларов США(USD): ");
// let y = +prompt("Введите валюту перевода(1 - EUR, 2 - UAH, 3 - AZN): ");
// if (y == 1){
//     let z = x * 0.93249;
//     console.log(`${z} EUR`)
// }
// else if (y == 2){
//     z = x * 36.95;
//     console.log(`${z} UAH`)
// }  
// else if (y == 3){
//     z = x * 1.7;
//     print(`${z} AZN`)
// } 
// else{
//     console.log("Ошибка!")
// }

// Задание 12

// x = +prompt("Введите сумму покупки, руб.: ")
// if (200 <= x && x < 300){
//     let y = x * 0.97;
//     console.log(`Ваша скидка 3%\nИтого к оплате ${y} руб.`)
// }
    
// else if (300 <= x && x < 500){
//     y = x * 0.95;
//     console.log(`Ваша скидка 5%\nИтого к оплате ${y} руб.`)
// }
// else if (x >= 500){
//     let y = x * 0.93;
//     console.log(`Ваша скидка 7%\nИтого к оплате ${y} руб.`)
// }

// else{
//     console.log(`Ваша скидка 0%\nИтого к оплате ${x} руб.`)
// }

// Задание 13

// let L = +prompt("Введите длину окружности, мм: ");
// let P = +prompt("Введите периметр квадрата, мм: ");
// let d = L / 3.14;
// let a = P / 4;
// if (d <= a){
//     console.log("Окружность поместится в квадрат")
// }
// else{
//     console.log("Окружность не поместится в квадрат")
// }
    
// Задание 14

// let x = +prompt("Самая длинная река в мире?\n1 - Амазонка\n2 - Нил\n3 - Миссисипи\nВведите вариант ответа (1,2,3): ");
// let score = 0;
// if (x == 1){
//     console.log("Ответ верный!")
//     score = score + 2
// }
// else{
//     console.log("Ответ неверный!")
// }

// let y = +prompt("Самая многочисленная страна в Европе?\n1 - Турция\n2 - Россия\n3 - Германия\nВведите вариант ответа (1,2,3): ");
// if (y == 2){
//     console.log("Ответ верный!")
//     score = score + 2
// }
// else{
//     console.log("Ответ неверный!")
// }

// let z = +prompt("Самая маленькая страна в мире?\n1 - Лихтенштейня\n2 - Монако\n3 - Ватикан\nВведите вариант ответа (1,2,3): ");
// if (z == 3){
//     console.log("Ответ верный!")
//     score = score + 2
// }
// else{
//     console.log("Ответ неверный!")
// }

// console.log(`Вы набрали ${score} очка(ов)`)

// Задание 15

// let d = +prompt("Введите дату (ДД): ")
// let m = +prompt("Введите месяц (ММ): ")
// let y = +prompt("Введите год (ГГГГ): ")
// if (m == 1 || m == 3 || m == 5 || m == 7 || m == 8 || m == 10){
//     if (d > 31){
//         console.log("Данные введены не верно!")
//     } 
//     else if (d == 31){
//         m = m + 1;
//         d = 1;
//         console.log(`${d}.${m}.${y}`)
//     }
//     else{
//         d = d + 1;
//         console.log(`${d}.${m}.${y}`)
//     } 
// }
    
// else if (m == 4 || m == 6 || m == 9 || m == 11){
//     if (d > 30){
//         console.log("Данные введены не верно!")
//     } 
//     else if (d == 30){
//         m = m + 1;
//         d = 1;
//         console.log(`${d}.${m}.${y}`)
//     }
//     else{
//         d = d + 1;
//         console.log(`${d}.${m}.${y}`)
//     }
// }
    
// else if (m == 2){
//     if (y % 4 == 0){
//         if (d > 29){
//             console.log("Данные введены не верно!")
//         }
//         else if (d == 29){
//             m = m + 1;
//             d = 1;
//             console.log(`${d}.${m}.${y}`)
//         }
//         else{
//             d = d + 1;
//             console.log(`${d}.${m}.${y}`)
//         }  
//     }
        
//     else{
//         if (d > 28){
//             console.log("Данные введены не верно!")
//         }
//         else if (d == 28){
//             m = m + 1;
//             d = 1;
//             console.log(`${d}.${m}.${y}`)
//         }
//         else{
//             d = d + 1;
//             console.log(`${d}.${m}.${y}`)
//         }
//     }
        
// }
    
// else if (m == 12){
//     if (d > 31){
//         console.log("Данные введены не верно!")
//     }
//     else if (d == 31){
//         m = 1;
//         d = 1;
//         y = y + 1;
//         console.log(`${d}.${m}.${y}`)
//     }
        
//     else{
//         d = d + 1;
//         console.log(`${d}${m}${y}`)
//     }
// }

// else{
//     console.log("Данные введены не верно!")
// }

// Задание 16

// let start = +prompt("Введите начало диапазона: ");
// let end = +prompt("Введите конец диапазона: ");
// for (i = start; i <= end; i++){
//     if (i % 7 == 0){
//         console.log(i)
//     }
// }

// Задание 17

// let start = +prompt("Введите начало диапазона: ");
// let end = +prompt("Введите конец диапазона: ");
// console.log("Все числа диапазона");
// for (i = start; i <= end; i++){
//     console.log(i)
// }          
// console.log("Все числа кратные 7");
// for (i = start; i <= end; i++){
//     if (i % 7 == 0){
//         console.log(i)
//     }       
// }
// console.log("Количество чисел кратных 5");
// let n = 1;
// for (i = start; i <= end; i++){
//     if (i % 5 == 0){
//         console.log(n);
//         n +=1
//     }  
// }
// console.log("Все числа диапазона в обратном порядке")
// for (i = start - 1; i <= end; i++){
//     console.log(end);
//     end = end - 1
// }    
    
// Задание 18

// let start = +prompt("Введите начало диапазона: ");
// let end = +prompt("Введите конец диапазона: ");
// while (start < end){
//     start++;
//     if (start % 3 == 0 && start % 5 != 0){
//         console.log("Fizz")
//     }
//     else if (start % 5 == 0 && start % 3 != 0){
//         console.log("Buzz")
//     }
//     else if (start % 3 == 0 && start % 5 == 0){
//         console.log("Fizz Buzz")
//     }
//     else if (start % 3 != 0 && start % 5 != 0){
//         console.log(start)
//     }
// }
    
// Задание 18

// console.log("Регистрация персонажа");
// let reg = 0;
// while (reg == 0){
//     let reg_gender = 0;
//     while (reg_gender == 0){
//         let gender = +prompt("Выберите пол персонажа\n1 - М\n2 - Ж\n>  ");
//         if (gender == 1){
//             gender = "Мужской";
//             reg_gender=1
//         } 
//         else if (gender == 2){
//             gender = "Женский";
//             reg_gender=1;
//         }
//         else{
//             console.log("Ошибка: Выберите из перечисленного")
//         }
//         if (reg_gender == 1){
//             let reg_race = 0;
//             while (reg_race == 0){
//                 let race = +prompt("Выберите рассу персонажа\n1 - Человек\n2 - Эльф\n3 - Гном\n4 - Назад\n5 - К началу\n>  ");
//                 if (race == 1){
//                     race = "Человек";
//                     reg_race = 1
//                 }  
//                 else if (race == 2){
//                     race = "Эльф";
//                     reg_race = 1
//                 }
//                 else if (race == 3){
//                     race = "Гном";
//                     reg_race = 1
//                 }
                    
//                 else if (race == 4){
//                     reg_gender = 0;
//                     break
//                 }
//                 else if (race == 5){
//                     reg_gender = 0
//                     break
//                 }
//                 else{
//                     console.log("Ошибка: Выберите из перечисленного")
//                 }
//                 if (reg_race == 1){
//                     reg_role = 0;
//                     if (race == "Человек"){
//                         while (reg_role == 0){
//                             let role = +prompt("Выберите роль пресонажа\n1 - Мечник\n2 - Лучник\n3 - Кавалерист\n4 - Назад\n5 - К началу\n>  ");
//                             if (role == 1){
//                                 role = "Мечник";
//                                 reg_role = 1
//                             }
//                             else if (role == 2){
//                                 role = "Лучник";
//                                 reg_role = 1
//                             }  
//                             else if (role == 3){
//                                 role = "Кавалерист";
//                                 reg_role = 1
//                             }
//                             else if (role == 4){
//                                 reg_race = 0
//                                 break
//                             }
//                             else if (role == 5){
//                                 reg_gender = 0;
//                                 break
//                             }
//                             else{
//                                 console.log("Ошибка: Выберите из перечисленного")
//                             }   
//                         }
//                     }
//                     else if (race == "Эльф"){
//                         while (reg_role == 0){
//                             let role = +prompt("Выберите роль пресонажа\n1 - Мечник\n2 - Лучник\n3 - Кавалерист\n4 - Назад\n5 - К началу\n>  ");
//                             if (role == 1){
//                                 role = "Мечник";
//                                 reg_role = 1
//                             }
//                             else if (role == 2){
//                                 role = "Лучник";
//                                 reg_role = 1
//                             } 
//                             else if (role == 3){
//                                 role = "Кавалерист";
//                                 reg_role = 1
//                             }
                                
//                             else if (role == 4){
//                                 reg_race = 0;
//                                 break
//                             }
                                
//                             else if (role == 5){
//                                 reg_gender = 0;
//                                 break
//                             }
//                             else{
//                                 console.log("Ошибка: Выберите из перечисленного")
//                             }
//                         }    
//                     }       
//                     else if (race == "Гном"){
//                         while (reg_role == 0){
//                             role = +prompt("Выберите роль персонажа\n1 - Мечник\n2 - Копейщик\n3 - Арбалетчик\n4 - Назад\n5 - К началу\n>  ");
//                             if (role == 1){
//                                 role = "Мечник";
//                                 reg_role = 1
//                             }
//                             else if (role == 2){
//                                 role = "Копейщик";
//                                 reg_role = 1
//                             }
//                             else if (role == 3){
//                                 role = "Арбалетчик";
//                                 reg_role = 1
//                             }
//                             else if (role == 4){
//                                 reg_race = 0;
//                                 break
//                             }
//                             else if (role == 5){
//                                 reg_gender = 0
//                                 break
//                             }
//                             else{
//                                 console.log("Ошибка: Выберите из перечисленного")
//                             }
                                
//                         }
                            
//                     }
                        
//                 }
                    
//             }
                
//         }
            
//     }
//     let myName = prompt("Введите имя: ");
//     let reg_name = 0;
//     while (reg_name == 0){
//         let info = +prompt("Вывести информацию о персонаже?\n1 - Да\n2 - Нет\n>  ");
//         if (info == 1){
//             console.log("Информация о персонаже: ");
//             console.log("Имя: ",myName);
//             console.log("Пол: ",gender);
//             console.log("Раса: ",race);
//             console.log("Роль: ",role);
//             break
//         }
//         else if (info == 2){
//             console.log("Персонаж не создан!");
//             break
//         }
//         else{
//             console.log("Ошибка: Выберите из перечисленного")
//         }       
//     }
//     reg+=1
// }

// Задание 19

let numberList = [5, 16, 7, 24, 3];
let numberList1 = [11, 3, 52, 5, 13];
console.log("Все элементы списков");
let numberList2 = [...numberList, ...numberList1];
console.log(numberList2);
console.log("------------------------------------");
console.log("Все элементы списков без повторений");
console.log(new Set(numberList2));
console.log("------------------------------------");
console.log("Общие элементы списков");
let numberList3 = [];
for (i of numberList){
    for (j of numberList1){
        if (i == j){
            numberList3.push(i);
            break
        }
    } 
}
console.log(numberList3);
console.log("------------------------------------");
console.log("Уникальные элементы списков");
let numberList4 = [];
for (i of numberList1){
    if (!(i in numberList)){
        numberList4.push(i);
    }  
}
for (i of numberList){
    if (!(i in numberList1)){
        numberList4.push(i);
    }
}
console.log(numberList4);
console.log("------------------------------------");
console.log("Максимальные и минимальные элементы обоих списков");
let numberList5 = [Math.max(...numberList), Math.min(...numberList), Math.max(...numberList1), Math.min(...numberList1)];
console.log(numberList5);
console.log("------------------------------------");