function getBold_items() {
    let bold_items = document.getElementsByTagName("strong")
    return bold_items
}

function highlight() {
    let strong_items = getBold_items()
    for (item of strong_items) {
        item.style.color = "blue"
    }
    return strong_items
}

function return_normal() {
    let strong_items = getBold_items()
    for (item of strong_items) {
        item.style.color = "black"
    }
    return strong_items
}

let strongs = document.getElementsByTagName("strong")
for (let i = 0; i < strongs.length; i++) {
    let blue = document.getElementsByTagName("strong")[i]
    blue.addEventListener("mouseover", highlight)
    blue.addEventListener("mouseout", return_normal)
}