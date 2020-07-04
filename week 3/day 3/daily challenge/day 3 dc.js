function only_letters() {
    let input = document.getElementsByTagName("input")[0];
    console.log(input.value);
    input.style.color = "blue"
    let inner_input = input.value
    if (inner_input.typeof != "String") {
        inner_input.remove()
    }
}