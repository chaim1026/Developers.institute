let numbers = []
let num1 = 0
let num2 = 0
let operater = ""
let error = "there was an error with your entries"

function number_clicked(number) {
    numbers.push(number)
}

function operater_clicked(symbol) {
    num1 = parseInt(numbers.join(""))
    numbers = []
    operater = symbol
}

function sum_of_nums() {
    num2 = parseInt(numbers.join(""))
    switch (operater) {
        case "+":
            console.log(num1 + num2)
            return num1 + num2
        case "-":
            console.log(num1 - num2)
            return num1 - num2
        case "/":
            if (num2 != 0) {
                console.log(num1 / num2)
                return num1 / num2
            } else {
                console.log(error)
                return error
            }
            default:
                return error

    }
}