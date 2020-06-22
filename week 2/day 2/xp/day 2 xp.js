// excersize 1

// let x = 5
// let y = 6
// if (5 < 6) {
//     console.log(y)
// } else {
//     console.log(x)
// }


// // excersize 2
// let newDog = 'Chihuahua'
// let numLetters = newDog.length
// console.log(numLetters)
// let upperCase = newDog.toUpperCase()
// console.log(upperCase)
// let lowerCase = newDog.toLowerCase()
// console.log(lowerCase)
// if (newDog === 'Chihuahua') {
//     console.log('I LOVE Chihuahua, it’s my favorite dog')
// } else {
//     console.log('I dont care, I prefer CATS')
// }


// excersize 3


// let num = prompt('please input a number')
// let num2 = parseInt(num)
// let value = num2
// if (value % 2 == 0) {
//     console.log(`${num2} is an even number`)
// } else {
//     console.log(`${num2} is not an even number`)
// }


// exersize 4


let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"]
let numOnline = prompt('enter number of people online')
let numOnline2 = parseInt(numOnline)
if (numOnline2 === 0) {
    console.log('no one online')
} else if (numOnline2 === 1) {
    console.log(`${users[0]} online`)
} else if (numOnline2 === 2) {
    console.log(`${users[1]} ${users[2]} online`)
} else if (numOnline2 > 2) {
    console.log(`${users[0]} ${users[1]} and ${numOnline2 - 2} more online`)
}