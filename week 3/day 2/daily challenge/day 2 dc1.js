let event1 = document.getElementById("num1")
let event2 = document.getElementById("num2")
let event3 = document.getElementById("num3")
let event4 = document.getElementById("num4")

event1.addEventListener("click", function () {
    event1.style.backgroundColor = "pink"
})

event2.addEventListener("mouseover", function () {
    event2.style.height = "150px"
    event2.style.width = "150px"
})

event3.addEventListener("mouseover", function () {
    event3.style.borderRadius = "50%"
})

event4.addEventListener("mouseout", function () {
    event4.style.boxShadow = "5px 10px grey"
})