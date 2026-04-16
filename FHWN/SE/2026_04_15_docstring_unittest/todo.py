def create_todo_list() -> list[dict]:
    """
    This function creates an empty todo list
    """
    return []

def add_new_task(todo:list[dict], task:dict):
    """Adds a new task to the todo list

    Args:
        todo (list[dict]): an existing todo list
        task (dict): a new task to be added
    """
    todo.append(task)

def pop_most_important_task(todo:list[dict]) -> dict|None:
    """Looks for the most important (highest priority) task, and returns & removes it from the todo list;

    Args:
        todo (list[dict]): the todo list

    Returns:
        dict|None: the most important task or None if empty
    
    Exceptions: Raises IndexError if called on an empty todo list
    """
    if len(todo) == 0: return None
    maxidx = 0
    for idx,task in enumerate(todo):
        if task["priority"] > todo[maxidx]["priority"]:
            maxidx = idx
    to_be_returned = todo[maxidx]
    del todo[maxidx]
    return to_be_returned

def is_empty(todo:list[dict]) -> bool:
    return len(todo) == 0

def number_of_tasks(todo:list[dict]) -> int:
    return len(todo)

def number_of_important_tasks(todo:list[dict], treshold:int) -> int:
    count = 0
    for task in todo:
        if task["priority"] >= treshold:
            count += 1
    return count
