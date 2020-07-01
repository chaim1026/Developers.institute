for (let i = 0; i < 4; i++) {
    let paragraph = document.getElementsByTagName("p")[i]
    paragraph.classList.add("para_article")
}

let remove = document.getElementsByClassName("para_article")[3]
remove.remove()

let h2 = document.getElementsByTagName("h2")[0]
h2.addEventListener("click", word_click)
h2.addEventListener("mouseover", hover)

function word_click(e) {
    h2.remove()
}

function hover(e) {
    h2.style.cursor = "pointer"
}

let h1 = document.getElementsByTagName("h1")[0]
h1.addEventListener("mouseover", fontsize)
h1.addEventListener("click", hide)


function fontsize(e) {
    h1.style.fontSize = Math.floor((Math.random() * 100) + 1) + "px"
}

function hide(e) {
    h1.style.visibility = "hidden"
}

let p2 = document.getElementsByTagName("p")[1]
p2.addEventListener("click", fade)

function fade(e) {
    p2.style.color = "blue"
    p2.style.fontSize = "20px"
    p2.style.transition = "all 2s"
}

let div = document.getElementsByTagName("div")[0]
let table = document.createElement("table")
div.appendChild(table)
let row = document.createElement("tr")
table.appendChild(row)
let col = document.createElement("td")
col.style.border = "1px solid green"
row.appendChild(col)
let col2 = document.createElement("td")
col2.style.border = "1px solid green"
row.appendChild(col2)
let input1 = document.getElementsByTagName("input")[0]
input1.oninput = function () {
    col.innerHTML = this.value
}

let input2 = document.getElementsByTagName("input")[1]
input2.oninput = function () {
    col2.innerHTML = this.value
}