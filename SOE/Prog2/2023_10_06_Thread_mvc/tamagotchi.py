from threading import Thread
from time import sleep


health = 10

def health_decreaser():
    global health
    while health != 0:
        sleep(3)
        health -= 1
        print(f"Health decreased to {health}")



timer_thread = Thread(target=health_decreaser, daemon=True)
timer_thread.start()

while True:
    print("""
        Mit szeretnel csinalni?
        1) Etetem
        2) Kilepek""")
    answer = int(input())
    if answer == 2: exit()
    elif answer == 1: 
        health += 3
        print(f"Megetetted, es a health felment {health}-re")