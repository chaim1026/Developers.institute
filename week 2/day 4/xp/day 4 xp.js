// excersize 1

// function check_driver_age() {
//     let age = prompt("What is your age ? ")

//     if (Number(age) < 18) {
//         alert("Sorry, you are too young to drive this car. Powering off");
//     } else if (Number(age) > 18) {
//         alert("Powering On. Enjoy the ride!")
//     } else if (Number(age) === 18) {
//         alert("Congratulations on your first year of driving. Enjoy the ride!");
//     }
// }
// check_driver_age()


// excersize 2

// amazon_basket = {
//     glasses: 1,
//     books: 2,
//     floss: 100
// }

// function check_basket() {
//     let item = prompt(`what item do you want`).toLowerCase()
//     if (item = amazon_basket[item]) {
//         alert(`your item is in the basket`)
//     } else {
//         alert(`your item is not in the basket`)
//     }
// }
// check_basket()


// function check_basket() {
//     let item = prompt("what item do u want")
//     for (let i in amazon_basket) {
//         if (item === i) {
//             console.log(alert("your item is in the basket"))
//             break
//         } else {
//             continue
//         }
//     }
//     console.log(alert("your item is not in the basket"))
// }
// check_basket()


// excersize 3


// function change_enough(pocket_change, price) {
//     let sum = 0
//     sum += pocket_change[0] * 0.25
//     sum += pocket_change[1] * 0.1
//     sum += pocket_change[2] * 0.5
//     sum += pocket_change[3] * 0.01

//     if (sum >= price) {
//         console.log("you have enough money")
//     } else {
//         console.log("you dont have enough money")
//     }
// }
// change_enough([4, 10, 20, 100], 1)


// excersize 4

// let shopping_list = ["banana", "orange", "apple"]
// let stock = {
//     "banana": 6,
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry": 1
// }

// let prices = {
//     "banana": 4,
//     "apple": 2,
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry": 10
// }
// let sum_of_prices = 0

// function my_bill() {
//     for (item of shopping_list) {
//         if (stock[item] > 0) {
//             sum_of_prices += prices[item]
//         }
//     }
//     return sum_of_prices
// }
// console.log(my_bill())


// excersize 5

function hotel_cost() {
    let nights = prompt("How many night would you like to stay in the hotel?")
    let cost = Number(nights) * 140
    return cost
}

let places = {
    "london": 183,
    "paris": 220,
    "other": 300
}

function plane_ride_cost() {
    let destination = prompt("What is your destination?")
    if (places[destination]) {
        return places[destination]
    } else {
        return places["other"]
    }
}

function rental_car_cost() {
    let num_of_days = prompt("How many days would you like to rent a car?")
    let cost = Number(num_of_days) * 40
    if (num_of_days > 10) {
        cost = cost * 0.95
    }
    return cost
}

function total_vacation_cost() {
    let total = hotel_cost() + plane_ride_cost() + rental_car_cost()
    console.log(total)
}
total_vacation_cost()