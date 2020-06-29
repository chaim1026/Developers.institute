document.getElementById("navBar").setAttribute("id", "socialNetworkNavigation")

let new_element = document.createElement("li")
let new_text = document.createTextNode("logout")
new_element.appendChild(new_text)
document.getElementById("list").appendChild(new_element)