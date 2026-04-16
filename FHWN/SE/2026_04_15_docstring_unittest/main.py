import random

from todo import * 


hausaufgabe = create_todo_list()
for i in range(10):
    add_new_task(hausaufgabe, {
        "priority" : random.randint(1,20),
        "description" : f"Hausaufgabe {i+1}"
    })

while not is_empty(hausaufgabe):
    task = pop_most_important_task(hausaufgabe)
    print(task)


next_task = pop_most_important_task(hausaufgabe)
if next_task is None:
    print("No more homework for you")
else:
    print(next_task)




