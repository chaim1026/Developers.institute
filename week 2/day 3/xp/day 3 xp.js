// let colors = ["blue", "green", "grey"]
// for (let i in colors) {
//     console.log(`my favorite color is : ${colors[i]}`)
//     console.log(`my # ${parseInt(i)+1} choice is ${colors[i]}`)
// }


// excersize 2

// let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]
// names.sort()
// let final_name = ""
// for (let name of names) {
//     final_name = final_name + name.charAt(0)
// }
// console.log(final_name)


// excersize 3

// let num = prompt("please enter a number")
// let newnum = parseInt(num)
// while (newnum < 10) {
//     newnum = prompt("please enter a new number")
// }


// excersize 4

// let people = ["Greg", "Mary", "Devon", "James"];
// people.shift()
// people.splice(2, 1, )
// people.splice(3, 0, "Jason")
// people.push("Chaim")
// let place = people.indexOf("Mary")
// console.log(place)
// let place2 = people.indexOf("Foo")
// console.log(place2)
// let last = people[people.length - 1]
// console.log(last)
// people = people.slice(1, 3)
// for (let i of people) {
//     if (i === "Mary") {
//         break
//     }
//     console.log(i)
// }


// excersize 5

let age = [20, 5, 12, 43, 98, 55]
let sum = 0
for (var i = 0; i < age.length; i++) {
    sum = sum + parseInt(age[i])
}
console.log(sum)