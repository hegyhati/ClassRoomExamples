import random

from todo import  *

def simple_test_with_2_tasks():
    todo = create_todo_list()
    task1 = {"priority" : 20, "description": "Task 1"}
    task2 = {"priority" : 4, "description": "Task 2"}
    add_new_task(todo, task1)
    add_new_task(todo, task2)
    next = pop_most_important_task(todo)
    print("OK" if next["description"] == "Task 1" else "ERROR")
    next = pop_most_important_task(todo)
    print("OK" if next["description"] == "Task 2" else "ERROR")

def simple_test_with_3_tasks():
    todo = create_todo_list()
    task1 = {"priority" : 20, "description": "Task 1"}
    task2 = {"priority" : 4, "description": "Task 2"}
    task3 = {"priority" : 44, "description": "Task 3"}
    task4 = {"priority" : -24, "description": "Task 4"}
    add_new_task(todo, task1)
    add_new_task(todo, task2)
    add_new_task(todo, task3)
    add_new_task(todo, task4)
    next = pop_most_important_task(todo)
    print("OK" if next["description"] == "Task 3" else "ERROR")

def test_pop_on_empty_list():
    todo = create_todo_list()
    task = pop_most_important_task(todo)
    print("OK" if task is None else "ERROR")

def test_task_count_with_random():
    count = random.randint(5,15)
    t = create_todo_list()
    for _ in range(count):
        add_new_task(t,{"descriotion":"", "priority":1})
    print("OK" if number_of_tasks(t) == count else "ERROR")
    print("OK" if number_of_important_tasks(t,1) == count else "ERROR")
    print("OK" if number_of_important_tasks(t,2) == 0 else "ERROR")
    
        
    

if __name__ == "__main__":
    simple_test_with_2_tasks()
    simple_test_with_3_tasks()
    test_pop_on_empty_list()
    test_task_count_with_random()