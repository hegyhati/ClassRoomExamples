var btnAdd = document.getElementById("btn");
var btnReset = document.getElementById("reset");
var inputs = document.querySelectorAll("input");

// Számol gombra kattintva összeadja az értékeket
btnAdd?.addEventListener("click", () => {
  // mindegyik pénzérmének külön változó plusz ezeket már előre beszoroztam amennyi a pénz értéke
  var num1 = parseInt(document.getElementById("forint5").value * 5);
  var num2 = parseInt(document.getElementById("forint10").value * 10);
  var num3 = parseInt(document.getElementById("forint20").value * 20);
  var num4 = parseInt(document.getElementById("forint50").value * 50);
  var num5 = parseInt(document.getElementById("forint100").value * 100);
  var num6 = parseInt(document.getElementById("forint200").value * 200);
  //itt adom össze őket
  var sum = num1 + num2 + num3 + num4 + num5 + num6;
  //összeg kiírása a final result ID-be
  document.getElementById("final-result").innerHTML = sum + " HUF";
});

//kis extra, törölni tudod az összes eddigi beírt értéket
btnReset?.addEventListener("click", () => {
  inputs.forEach((input) => (input.value = ""));
  document.getElementById("final-result").innerHTML = "";
});
