function new_guess(){
    let secret_word = "apple"
    let guess = document.getElementById("guess_word").value
    if (guess==secret_word){
        document.getElementById("feedback").innerHTML = "Grat, nyertel!"
    } else {
        document.getElementById("feedback").innerHTML = "Nem jo!"
    }
    document.getElementById("history").innerHTML += "<li>"+guess+"</li>"
}