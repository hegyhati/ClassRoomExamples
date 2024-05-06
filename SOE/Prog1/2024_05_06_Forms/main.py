import os
import json
import datetime
import matplotlib.pyplot as plt

FORM_DIR = "Forms"

menu_options = [
    "Formok listazasa",
    "Uj form letrehozasa",
    "Meglevo form kitoltese",
    "Statisztika kitoltott form-hoz",
    "Kilepes"
]

def menu_select():
    print()
    for i, option in enumerate(menu_options):
        print(f"{i+1}. {option}")
    return int(input("Melyiket valasztod? "))

def get_meta(file):
    with open(os.path.join(FORM_DIR, file)) as f:
            data = json.load(f)
    return data['meta']

def list_forms():
    print("Elerheto formok:")
    for file in os.listdir(FORM_DIR):
        meta = get_meta(file)
        print(f" {file}: {meta['description']} ({meta['creation_date']})")  

question_types = ["text", "number"]
        
def create_new_form():
    description = input("Mi a leirasa a formnak? ")
    questions = []
    while True:
        response = input("Szeretnel tovabbi kerdest hozzaadni? ")
        if response.lower() == "nem" : break
        type = input(f"Milyen tipusu kerdes legyen? {'/'.join(question_types)} ")
        text = input("Mi legyen a kerdes szovege? ")
        questions.append({
            "type" : type,
            "text" : text
        })
    filename = input("Mi legyen a fajl neve? ")+".json"
    with open(os.path.join(FORM_DIR,filename), "w") as f:
        json.dump({
            "meta" : {
                "description" : description,
                "creation_date" : str(datetime.datetime.now())
            },
            "questions" : questions,
            "answers" : []
        },f)    
        

def fill_form():
    list_forms()
    form = input("Melyiket szeretned kitolteni? ")
    with open(os.path.join(FORM_DIR, form)) as f:
        data = json.load(f)
    print()
    print()
    print(data["meta"]["description"])
    print()
    responses = []
    for question in data['questions']:
        response = input(question['text']+ " ")
        if question["type"] == "number":
            response = int(response)
        responses.append(response)
    data["answers"].append(responses)
    with open(os.path.join(FORM_DIR,form), "w") as f:
        json.dump(data,f)


def simple_bar_plot():
    list_forms()
    form = input("Melyikbol szeretnel statisztikat csinalni? ")
    with open(os.path.join(FORM_DIR, form)) as f:
        data = json.load(f)
    print("Kerdesek:")
    for i,question in enumerate(data["questions"]):
       print(f"{i}: {question}") 
    x_id = int(input("Melyik legyen a label set? "))
    height_id = int(input("Melyikbol legyenek az adatok? "))
    
    x = [response[x_id] for response in data["answers"]]
    height = [response[height_id] for response in data["answers"]]
    fig,ax = plt.subplots()
    ax.bar(x,height)
    fig.suptitle(data["questions"][height_id]["text"])
    fname,ext = os.path.splitext(form)
    fig.savefig(os.path.join(FORM_DIR,fname+f"_{x_id}_{height_id}.png"))
    
while True:
    response = menu_select()
    match response:
        case 1: list_forms()
        case 2: create_new_form()
        case 3: fill_form()
        case 4: simple_bar_plot()
        case 5: exit()