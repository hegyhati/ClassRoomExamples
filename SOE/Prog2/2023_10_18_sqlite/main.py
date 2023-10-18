from manager import DB_Manager
from manager import Team,Runner

def new_runner():
    name = input("Name of runner: ")
    team = input("Team: ")
    return Runner(name,team)

dbm = DB_Manager()

for team in [
    Team("VeszpRUN", "Veszprem", "orange", 2013),
    Team("Futokalandorok", "Gyor", "lime", 2017),
    Team("Loholo duhajok", "Sopron", "orange", 2021)
] : dbm.persist(team)


while True:
    response = input("""What do you want?
                     r) Add new runner
                     x) Exit
                     """)
    if response == "x": break
    if response == "r":
        runner = new_runner()
        dbm.persist(runner)
