
function szamol ()  {
  // mindegyik pénzérmének külön változó plusz ezeket már előre beszoroztam amennyi a pénz értéke
  let num1 = Number(document.getElementById("forint5").value) * 5;
  let num2 = Number(document.getElementById("forint10").value) * 10;
  let num3 = Number(document.getElementById("forint20").value) * 20;
  let num4 = Number(document.getElementById("forint50").value) * 50;
  let num5 = Number(document.getElementById("forint100").value) * 100;
  let num6 = Number(document.getElementById("forint200").value) * 200;
  //itt adom össze őket
  let sum = num1 + num2 + num3 + num4 + num5 + num6;
  //összeg kiírása a final result ID-be
  document.getElementById("final-result").innerHTML = sum + " HUF";
}

function torol() {
  document.getElementById("forint5").value = ""
  document.getElementById("forint10").value = ""
  document.getElementById("forint20").value = ""
  document.getElementById("forint50").value = ""
  document.getElementById("forint100").value = ""
  document.getElementById("forint200").value = ""

}