let sentence = prompt("please enter several words (separated by commas) ")
let words = sentence.split(",")
for (i in words) {
    words[i] = words[i].trim()
}

function get_longest_word() {
    let longest = 0
    for (word of words) {
        if (word.length > longest) {
            longest = word.length
        }
    }
    return longest
}
longest = get_longest_word()
// let longest = 0
// for (word of words) {
//     if (word.length > longest) {
//         longest = word.length
//     }
// }
let star_line = "*".repeat(longest + 4)
console.log(star_line)
for (word of words) {
    console.log("* " + word + " ".repeat(longest - word.length + 1) + "*")
}
console.log(star_line)