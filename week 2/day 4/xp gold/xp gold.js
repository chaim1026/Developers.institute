let user_number = 0
let computer_number = 0


function play_the_game() {
    let question = confirm("Would you like to play the game?")
    if (question == false) {
        alert("no problem goodbye")
    } else {
        let number1 = prompt("please enter a number from 0 to 10")
        user_number = parseFloat(number1)
        if (Number.isInteger(user_number) && user_number >= 0 && user_number < 11) {
            computer_number = Math.floor(Math.random() * 11)
            console.log(user_number)
            console.log(computer_number)
            test(user_number, computer_number)
        } else if (Number.isInteger(user_number) && user_number < 0 || Number.isInteger(user_number) && user_number > 10) {
            alert("Sorry it’s not a good number, Goodbye")
        } else {
            alert("sorry not a number, goodbye")
        }
    }
}

function test(x, y) {
    if (x == y) {
        alert("you won the game")
    }
    for (let i = 1; i <= 3; i++) {
        if (x > y) {
            x = prompt("your number is bigger then the computer _number please guess again ")
            x = parseFloat(x)
            if (x == y) {
                alert("you won the game")
                break
            } else {
                alert("you did not guess correctly")
            }
        } else if (x < y) {
            x = prompt("your number is smaller then the computer _number please guess again ")
            x = parseFloat(x)
            if (x == y) {
                alert("you won the game")
                break
            } else {
                alert("you did not guess correctly")
            }
        }
    }
}