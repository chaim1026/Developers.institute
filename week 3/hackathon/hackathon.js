let color_array = ["#003366", "#336699", "#003399", "#000066", "#006699", "#006666", "#669999", "#009999", "#33cccc", "#666699", "#00ffff", "#00cc99", "#339966", "#9933ff", "#00ff99", "#00cc66", "#cc66ff", "#00ff00", "#66ff66", "#ccffcc", "#ffffff", "#ff66ff", "#cc00cc", "#993399", "#ff33cc", "#99ff66", "#66ff33", "#99ff33", "#ffff99", "#ff9999", "#ff3399", "#cc6699", "#cc0066", "#660033", "#ff6600", "#ffff00", "#999966", "#996633", "#ff9900", "#ff0000", "#cc0000", "#990033", "#993333", "#800000", "#990000", "#993300", "#cc3300"]


let i = 0
for (i = 0; i <= 19999; i++) {
    let div = document.createElement("div")
    let wrapper = document.getElementById("wrapper")
    wrapper.appendChild(div)
    div.style.width = "5px"
    div.style.height = "5px"
    div.addEventListener("mouseover", color)

    function color(event) {
        if (event.buttons == 1)
            div.style.backgroundColor = color_choice.value
    }
}

let color_choice = document.getElementById("pick_color")

let button = document.getElementById("background_color")
button.addEventListener("click", function () {
    let get_wrapper = document.getElementById("wrapper")
    get_wrapper.style.backgroundColor = color_array[Math.floor(Math.random() * 47)]
})

let wrapper = document.getElementById("wrapper")
wrapper.addEventListener("mouseover", function () {
    wrapper.style.cursor = "grabbing"
})
setInterval(function () {
    wrapper.style.borderBottomColor = color_array[Math.floor(Math.random() * 47)]
    wrapper.style.borderTopColor = color_array[Math.floor(Math.random() * 47)]
    wrapper.style.borderRightColor = color_array[Math.floor(Math.random() * 47)]
    wrapper.style.borderLeftColor = color_array[Math.floor(Math.random() * 47)]
}, 1000)

let direction = document.getElementById("direction")
direction.addEventListener("click", function () {
    alert("1: Choose a background color 2: Select a color 3: To color press down and move your mouse 4: To erase remove selected color and press mouse down and hover over your mistake 5: Press refresh canvas to get a blank canvas 6: Have fun!!!")
})

let headline = document.getElementById("headline")
headline.style.textAlign = "center"
headline.style.fontSize = "50px"
setInterval(function () {
    headline.style.color = color_array[Math.floor(Math.random() * 47)]
}, 1000)