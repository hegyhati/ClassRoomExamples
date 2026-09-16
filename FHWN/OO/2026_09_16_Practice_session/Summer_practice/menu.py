from practice_json_manager import *

print("asdfasdfasdf")


while True:
    selection = int(input("""
    What do you want to do?
        1. list practices for a subject
        2. register new practice hours
        3. quit
        """))
    match selection:
        case 1: 
            subject = input("Subject: ")
            print_practices_for_subject(subject)
        case 2:
            register_new_practice()
        case 3: break
        case _: print("Incorrect answer, please chose 1-3.")