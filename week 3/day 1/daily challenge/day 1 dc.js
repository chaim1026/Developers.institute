let all_books = [
    book1 = {
        title: "kane and able",
        auther: "Jeffery Archer",
        image: "https://kbimages1-a.akamaihd.net/16cb11f0-6011-4d3a-b4a1-f4802222f0ae/1200/1200/False/kane-and-abel.jpg",
        already_read: true
    },

    book2 = {
        title: "sins of the father",
        auther: "Jeffery Archer",
        image: "https://images-na.ssl-images-amazon.com/images/I/91kzUenRPEL.jpg",
        already_read: true
    }
]

let tab_table = document.createElement("table")
for (let book in all_books) {
    let tab_tr = document.createElement("tr")
    for (let i = 0; i <= 3; i++) {
        let tab_td = document.createElement("td")
        tab_td.style.paddingRight = "20px"
        let text = ""
        let image
        if (i == 0) {
            text = document.createElement("h3")
            text.innerHTML = all_books[book].title
            if (all_books[book].already_read == true) {
                text.style.color = "red"
            }
            tab_td.appendChild(text)
        } else if (i == 1) {
            text = document.createElement("h3")
            text.innerHTML = "written by:"
            if (all_books[book].already_read == true) {
                text.style.color = "red"
            }
            tab_td.appendChild(text)
        } else if (i == 2) {
            text = document.createElement("h3")
            text.innerHTML = all_books[book].auther
            if (all_books[book].already_read == true) {
                text.style.color = "red"
            }
            tab_td.appendChild(text)
        } else {
            image = document.createElement("img")
            image.setAttribute("src", all_books[book].image)
            image.style.width = "100px"
            tab_td.appendChild(image)
        }
        tab_tr.appendChild(tab_td)
        tab_table.appendChild(tab_tr)
    }
}
document.body.appendChild(tab_table)