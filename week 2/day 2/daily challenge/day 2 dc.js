let string = prompt("please enter a sentence with both not and bad")
let array = string.split(" ")
let position1 = array.indexOf("not")
let position2 = array.indexOf("bad")
console.log(position1)
console.log(position2)
if (position1 < position2 && position1 > -1) {
    array.splice(position1, position2 - position1 + 3, "good")
    string = array.join(" ")
    console.log(" ")
}
console.log(string)