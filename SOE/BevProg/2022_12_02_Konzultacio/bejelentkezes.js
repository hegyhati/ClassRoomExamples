function check_login() {
    let user_data = [
        { "username": "zita", "password": "kiscica" },
        { "username": "fanni", "password": "hovirag" },
        { "username": "vivi", "password": "jelszo" },
        { "username": "laci", "password": "l4c1" }
    ] // JSON


    let username = document.getElementById("user_name").value


    let user_idx = -1
    for (let idx = 0; idx < user_data.length; idx++) {
        if (user_data[idx]["username"] == username) {
            user_idx = idx
        }
    }
    //let user_idx = user_data.findindex((user) => user[0]==username)

    if (user_idx == -1) {
        document.getElementById("message").innerHTML = "Nincs ilyen felhasznalo a rendszerben."
    } else {
        let password = document.getElementById("user_password").value
        if (password == user_data[user_idx]["password"]) {
            document.getElementById("message").innerHTML = "Sikerult belepni!"
            document.getElementById("login_fields").innerHTML = ""
        } else {
            document.getElementById("message").innerHTML = "Nincs jogosultsagod."
        }
    }
}

