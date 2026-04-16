import random
import unittest

from todo import  *

class MyUnitTestsForTodo(unittest.TestCase):
    def test_simple_test_with_2_tasks(self):
        todo = create_todo_list()
        task1 = {"priority" : 20, "description": "Task 1"}
        task2 = {"priority" : 4, "description": "Task 2"}
        add_new_task(todo, task1)
        add_new_task(todo, task2)
        self.assertEqual(pop_most_important_task(todo)["description"], "Task 1")
        self.assertEqual(pop_most_important_task(todo)["description"], "Task 2")

    def test_simple_test_with_3_tasks(self):
        todo = create_todo_list()
        task1 = {"priority" : 20, "description": "Task 1"}
        task2 = {"priority" : 4, "description": "Task 2"}
        task3 = {"priority" : 44, "description": "Task 3"}
        task4 = {"priority" : -24, "description": "Task 4"}
        add_new_task(todo, task1)
        add_new_task(todo, task2)
        add_new_task(todo, task3)
        add_new_task(todo, task4)
        self.assertEqual(pop_most_important_task(todo)["description"], "Task 3")

    def test_pop_on_empty_list(self):
        todo = create_todo_list()
        self.assertIsNone(pop_most_important_task(todo))

    def test_task_count_with_random(self):
        count = random.randint(5,15)
        t = create_todo_list()
        for _ in range(count):
            add_new_task(t,{"description":"", "priority":1})
        self.assertEqual(number_of_tasks(t),count)
        self.assertEqual(number_of_important_tasks(t,1),count)
        self.assertEqual(number_of_important_tasks(t,2),0)

if __name__ == "__main__":
    unittest.main(verbosity=0)