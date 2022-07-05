import json
from random import randint, sample


with open('rooms.json') as f:
    rooms = json.load(f)

names = {person for room in rooms for person in room['people']}


logs = [
    {
        'id' : name,
        'direction' :  event[0],
        'date' : f"2022-03-{day:02}",
        'timestamp': f"{event[1]:06}"
    }
    for name in names
    for day in sample(set(range(1,30)), k=randint(5,20))
    for event in zip(['in', 'out'],sorted([randint(21600,75600),randint(21600,75600)]))
]

logs.sort(key=lambda log: log['date']+f"-{log['timestamp']}")

with open('log.csv', 'w') as f:
    for log in logs:
        f.write(f"{log['date']},{log['timestamp']},{log['id']},{log['direction']}\n")

