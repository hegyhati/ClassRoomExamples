function check_login(){
    let users = ["zita", "fanni", "vivi", "laci", "feri", "mate"]
    let passwords = ["kiscica", "hovirag", "jelszo", "l4c1", "qork,-lsdfj", "meh"]


    let username = document.getElementById("user_name").value
    let user_idx = users.indexOf(username)

    if (user_idx == -1) {  
        document.getElementById("message").innerHTML = "Nincs ilyen felhasznalo a rendszerben."
    } else {
        let password = document.getElementById("user_password").value
        if (password==passwords[user_idx]) {
            document.getElementById("message").innerHTML =  "Sikerult belepni!"
            document.getElementById("login_fields").innerHTML =  ""
        } else {
            document.getElementById("message").innerHTML = "Nincs jogosultsagod."
        }
    } 
}

