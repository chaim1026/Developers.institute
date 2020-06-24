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
//     for (let item of shopping_list) {
//         if (stock[item] > 0) {
//             sum_of_prices += parseFloat(prices[item])
//         }
//     }
//     return sum_of_prices
// }
// console.log(my_bill())

// excersize 5

function hotel_cost() {
    let nights = prompt("how many night would you like to stay at the hotel")
    let payment = Number(nights) * 140
    console.log(payment)
    return (payment)
}
// hotel_cost()

let destination = {
    "london": 183,
    "paris": 220,
}

function plane_ride_cost() {
    let user_destination = prompt("what is your destination")
    if (destination[user_destination]) {
        console.log(destination[user_destination])
        return (destination[user_destination])
    } else {
        console.log(300)
        return (300)
    }
}
// plane_ride_cost()

function rental_car_cost() {
    let days = prompt("how many days would you like to rent the car")
    days = Number(days)
    if (days <= 10) {
        console.log(days * 40)
        return (days * 40)
    } else {
        console.log((days * 40) * 0.95)
        return ((days * 40) * 0.95)
    }
}
// rental_car_cost()

function total_vacation_cost(hotel, plane, car) {
    let total = 0
    total += hotel
    total += plane
    total += car

    console.log(total)
    return total
}
total_vacation_cost(hotel_cost(), plane_ride_cost(), rental_car_cost())