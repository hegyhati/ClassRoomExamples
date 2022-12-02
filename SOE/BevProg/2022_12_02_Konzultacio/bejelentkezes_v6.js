function check_login(){
    let user_data = [
        ["zita", "kiscica"],
        ["fanni", "hovirag"],
        ["vivi", "jelszo"],
        ["laci", "l4c1"]
    ]
    

    let username = document.getElementById("user_name").value
    

    let user_idx = -1
    for (let idx = 0; idx < user_data.length; idx++) {
        if (user_data[idx][0] == username) {
            user_idx = idx
        }
    }
    //let user_idx = user_data.findindex((user) => user[0]==username)

    if (user_idx == -1) {  
        document.getElementById("message").innerHTML = "Nincs ilyen felhasznalo a rendszerben."
    } else {
        let password = document.getElementById("user_password").value
        if (password==user_data[user_idx][1]) {
            document.getElementById("message").innerHTML =  "Sikerult belepni!"
            document.getElementById("login_fields").innerHTML =  ""
        } else {
            document.getElementById("message").innerHTML = "Nincs jogosultsagod."
        }
    } 
}

