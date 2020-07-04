let stars = "    *"
console.log(stars)
for (let i = 0; i < 4; i++) {
    let adding_star = "**"
    stars = stars.concat(adding_star)
    stars = stars.substr(1)
    console.log(stars)
}