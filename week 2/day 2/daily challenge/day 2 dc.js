let string = 'the train ride to school was not that bad today'
let array = string.split(" ")
let position1 = array.indexOf("not")
let position2 = array.indexOf("bad")
console.log(position1)
console.log(position2)
if (position1 < position2) {
    console.log('the train ride to school was good')
} else {
    console.log(string)
}