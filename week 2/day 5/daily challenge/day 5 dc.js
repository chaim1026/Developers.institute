let number = prompt("please input a number lower then 100")
let number2 = parseFloat(number)
let subtract = 0
while (number2 >= 1) {
    if (subtract == 0) {
        subtract = subtract + 1
        console.log(`${number2} bottles of beer on the wall
        ${number2} bottles of beer
        Take ${subtract} down, pass it around
        ${number2 - subtract} bottles of beer on the wall`)
        number2 = number2 - subtract

    } else if (number2 == 1) {
        subtract = subtract + 1
        console.log(`${number2} bottle of beer on the wall
        ${number2} bottle of beer
        Take it down, pass it around
        0 bottles of beer on the wall`)
        number2 = number - subtract

    } else if (number2 < subtract && number2 > 0) {
        subtract = number2
        console.log(`${number2} bottle of beer on the wall
        ${number2} bottle of beer
        Take them down, pass them around
        0 bottles of beer on the wall`)
        number2 = number - subtract
        break

    } else if (number2 > 0 && number2 > subtract) {
        subtract = subtract + 1
        console.log(`${number2} bottles of beer on the wall
        ${number2} bottles of beer
        Take ${subtract} down, pass them around
        ${number2 - subtract} bottles of beer on the wall`)
        number2 = number2 - subtract
    }
}