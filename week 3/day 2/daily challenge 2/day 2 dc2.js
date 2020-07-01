let value1 = document.getElementsByTagName("input")[0]
value1.oninput = function () {
    value1.innerHTML = this.value
}

let value2 = document.getElementsByTagName("input")[1]
value2.oninput = function () {
    value2.innerHTML = this.value
}

let value3 = document.getElementsByTagName("input")[2]
value3.oninput = function () {
    value3.innerText = this.value
}