function distance() {
    document.getElementById("meter").innerHTML =
        0.3048 * Number(document.getElementById("foot").value) +
        0.0254 * Number(document.getElementById("inch").value)
}

function temperature() {
    document.getElementById("celsius").innerHTML =
        (Number(document.getElementById("fahrenheit").value) - 32 ) / 1.8
}

function EN() {
    document.getElementById("foot_name").innerHTML = "feet"
    document.getElementById("inch_name").innerHTML = "inches"
}

function HU() {
    document.getElementById("foot_name").innerHTML = "láb"
    document.getElementById("inch_name").innerHTML = "hüvelyk"
}