let users = ["zita", "fanni", "vivi", "laci", "feri", "mate"]
let passwords = ["kiscica", "hovirag", "jelszo", "l4c1", "qork,-lsdfj", "meh"]


let username = prompt("username:")
let user_idx = users.indexOf(username)

if (user_idx == -1) {  
    alert("Nincs ilyen felhasznalo a rendszerben.")
} else {
    let password = prompt("password:")
    if (password==passwords[user_idx]) {
        alert("Sikerult belepni!")
    } else {
        alert("Nincs jogosultsagod.")
    }
} 
