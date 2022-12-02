let users = ["zita", "fanni", "vivi", "laci", "feri", "mate"]
let passwords = ["kiscica", "hovirag", "jelszo", "l4c1", "qork,-lsdfj", "meh"]


let username = prompt("username:")
let user_exists = false
for (let idx = 0; idx<users.length; idx++){
    if (username == users[idx]) {
        user_exists = true
    }
}

if (user_exists) {  
    let password = prompt("password:")
    let user_idx = -1
    for (let idx = 0; idx<users.length; idx++){
        if (username == users[idx]) {
            user_idx = idx
        }
    }
    if (password==passwords[user_idx]) {
        alert("Sikerult belepni!")
    } else {
        alert("Nincs jogosultsagod.")
    }
} else {
    alert("Nincs ilyen felhasznalo a rendszerben.")
}
