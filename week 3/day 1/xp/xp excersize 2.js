document.getElementsByTagName("li")[1].innerHTML = "Richard"
document.getElementsByTagName("li")[0].innerHTML = "Chaim"
document.getElementsByTagName("li")[2].innerHTML = "Chaim"

let new_element = document.createElement("li")
let new_text = document.createTextNode("Hey Students")
new_element.appendChild(new_text)
document.getElementById("a").appendChild(new_element)

let new_element2 = document.createElement("li")
let new_text2 = document.createTextNode("Hey Students")
new_element2.appendChild(new_text2)
document.getElementById("b").appendChild(new_element2)

let item = document.getElementById("name")
item.parentNode.removeChild(item)