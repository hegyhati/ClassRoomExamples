/*

INITIAL DATA 

Later will be replaced by an http request to backend.

*/

let patients = [
    {
      "name": "Bilbo Baggins",
      "SSN": "1234"
    },
    {
      "name": "Frodo Baggins",
      "SSN": "5678"
    },
    {
      "name": "Gandalf the Grey",
      "SSN": "9012"
    },
    {
      "name": "Aragorn Strider",
      "SSN": "3456"
    },
    {
      "name": "Legolas Greenleaf",
      "SSN": "7890"
    },
    {
      "name": "Gimli Lockbeard",
      "SSN": "1357"
    },
    {
      "name": "Boromir of Gondor",
      "SSN": "2468"
    },
    {
      "name": "Samwise Gamgee",
      "SSN": "3579",
    },
    {
      "name": "Meriadoc Brandybuck",
      "SSN": "4680",
    },
    {
      "name": "Peregrin Took",
      "SSN": "5791",
    },
    {
      "name": "Gollum Sméagol",
      "SSN": "6802",
    }
]

/*

BEHAVIOR
Functions that maintain the above structure in memory, and update the DOM accordingly.

*/

// Simple checkers for data consistency - note 2 forms of object attribute access

function name_exist(name) {
    return patients.some(patient => patient.name == name)
}

function ssn_exist(name) {
    return patients.some(patient => patient["SSN"] == name)
}

// Responsible to add a patient to DOM 
// Called by both initializer and new patient addition
function add_patient_to_DOM (patient) {    
    const table = document.getElementById("patient_table");
    const row = document.createElement("tr");
    row.setAttribute("id", patient.ssn)
    const nameCell = document.createElement("td");
    nameCell.textContent = patient.name;
    const ssnCell = document.createElement("td");
    ssnCell.textContent = patient.SSN;
    row.appendChild(nameCell);
    row.appendChild(ssnCell);
    table.appendChild(row);
}

// Function to add new patient to both data structure and DOM
function add_patient(name, ssn) {
    new_patient = {
        "name" : name,
        "SSN" : ssn
    }
    patients.push(new_patient)
    add_patient_to_DOM(new_patient)    
}


// Event handler for form submission
function add_patient_form_submission(){
    const name = document.getElementById("name").value
    const ssn = document.getElementById("ssn").value

    if (name_exist(name)) {
        alert(`Patient with name ${name} already exists.`)
        return
    }
    if (ssn < 1000 || ssn > 9999) {
        alert("Invalid SSN!")
        return

    }
    if (ssn_exist(ssn)) {
        alert("Another patient already has this SSN.")
        return
    }
    
    add_patient(name,ssn)
}


/*

INITIALIZATION
Runs when the page is loaded - note defer in <script> tag in the html

*/

// Assigns the above function to the form submission and suppresses page reload
document.getElementById("new_patient").addEventListener("submit", function(event) {
    event.preventDefault();
    add_patient_form_submission();
});
// Adds all existing patients to the DOM
for (patient of patients) add_patient_to_DOM(patient)