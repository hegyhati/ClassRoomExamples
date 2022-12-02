let moves = prompt("Mozog? (I/N)")

if (moves == "I" || moves == "i") {
    let should = prompt("Kéne?")
    if (should == "I" || should == "i") {
        alert("Remek, semmi probléma")
    } else if (should == "N" || should == "n") {
        alert("Íme, némi ragasztószalag")
    } else { 
        alert("Rossz válasz!") 
    }
} else if (moves == "N" || moves == "n") {
    let should = prompt("Kéne?")
    if (should == "I" || should == "i") {
        alert("Íme, némi WD-40")
    } else if (should == "N" || should == "n") {
        alert("Remek, semmi probléma")
    } else { 
        alert("Rossz válasz") 
    }
} else {
    alert("Rossz válasz")
}
