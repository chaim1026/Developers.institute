// excersize 1 

//     5 >= 1 //true 5 is bigger then 1
//     0 === 1 //false 0 does nit equal 1
//     4 <= 1 //false 1 is not great or equal to 4
//     1 != 1 //false 1 does equal 1
//     "A" > "B" //false the ascii of b is bigger
//     "B" < "C" //true same reason
//     "a" > "A" //true lowercase value is higher
//     "b" < "A" //false same reason
//     true === false //false true does not equal true
//     true != true //false true does = true


// excersize 2

// let c
// let a = 34
// let b = 21
// a = 2
// a + b = 23
// c = to nothing since we havent set a value yet
// console.log(3 + 4 + '5')

// excersize 3

// let numbers = prompt("please enter a number and separate them by a comma and space")
// let new_num = numbers.split(", ")
// let sum = 0
// for (num of new_num) {
//     sum += Number(num)
// }
// console.log(sum)

//ezcersize 4

let n = prompt("please enter a number")
let number = Number(n)
let string = ""
let string2 = "o"
let new_string = ""
let final = ""
let uppercase1 = ""
for (let i = 0; i < number; i++) {
    if (number < 2) {
        console.log("boom")
    } else if (number % 2 == 0 && number % 5 != 0) {
        new_string += string.concat(string2)
        final = `b${new_string}m!`
        uppercase1 = final
    } else if (number % 5 == 0 && number % 2 != 0) {
        new_string += string.concat(string2)
        final = `b${new_string}m`
        uppercase1 = final.toUpperCase()
    } else if (number % 2 == 0 && number % 5 == 0) {
        new_string += string.concat(string2)
        final = `b${new_string}m!`
        uppercase1 = final.toUpperCase()
    } else {
        new_string += string.concat(string2)
        final = `b${new_string}m`
        uppercase1 = final
    }
}
console.log(uppercase1)