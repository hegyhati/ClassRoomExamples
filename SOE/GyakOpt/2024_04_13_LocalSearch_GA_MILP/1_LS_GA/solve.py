import json
import sys
import random
from statistics import mean

with open(sys.argv[1]) as f:
    data = json.load(f)

people = list(data.keys())
tasks = list(data[people[0]].keys())

listdata = [
    {
        "name" : person,
        **data[person]
    }
    for person in people
]

def load(do, person):
    sumtime = 0
    for task in do[person]:
        sumtime += data[person][task]
    return sumtime

def makespan(do):
    makespan = 0
    for person in do:
        if load(do, person)>makespan: 
            makespan = load(do, person)
    return makespan    

def pretty_print_solution(do):
    for person in do:
        print(f"{person} [{load(do,person)}]: {do[person]}")
    print(f"MAKESPAN: {makespan(do)}")

def BenedekStrategy():
    do = {person: [] for person in people}
    for task in tasks:
        selected = min(listdata, key= lambda x: x[task])
        do[selected["name"]].append(task)
    return do

def reassign_task(do, giver, receiver, task):
    do[giver].remove(task)
    do[receiver].append(task)

def reassign_task_if_improves(do, giver, receiver, task):
    current = max(load(do,giver), load(do,receiver))
    reassign_task(do,giver,receiver,task)
    new = max(load(do,giver), load(do,receiver))
    if new >= current:
        reassign_task(do,receiver,giver,task)
        return False
    return True

def random_solution():
    tmp = {person : [] for person in people}
    for task in tasks:
        tmp[random.choice(people)].append(task)
    return tmp

def EsztiImproves(do):
    counter = 0
    while True:
        try: 
            for giver in people:
                for task in do[giver][:]:
                    for receiver in people:
                        if receiver != giver:
                            if reassign_task_if_improves(do, giver,receiver, task):
                                counter +=1
                                raise "yeppeee"
            break
        except:
            pass        
    return counter


def EsztiTabuImproves(do, visited):
    counter = 0
    visited.add(hash(do))
    while True:
        try: 
            for giver in people:
                for task in do[giver][:]:
                    for receiver in people:
                        if receiver != giver:
                            if reassign_task_if_improves(do, giver,receiver, task):
                                counter +=1
                                raise "yeppeee"
            break
        except:
            new = hash(do)
            if new in visited:
                return counter
            visited.add(new)
    return counter

def hash(do):
    s = ""
    for person in people:
        s += person
        do[person].sort()
        s += "".join(do[person])
    return s



def iterative_local_search():
    currentbest = 9999
    counter = 0
    solutioncounter = 0
    while True:
        counter += 1
        rnd = random_solution()
        solutioncounter += EsztiImproves(rnd)
        if counter % 100 == 0:
            print(counter, solutioncounter)
        if makespan(rnd) < currentbest:
            currentbest = makespan(rnd)
            pretty_print_solution(rnd)
    


def tabu_search():
    currentbest = 9999
    counter = 0
    solutioncounter = 0
    visited = set()
    while True:
        counter += 1
        rnd = random_solution()
        visited.add(hash(rnd))
        solutioncounter += EsztiTabuImproves(rnd,visited)
        if counter % 100 == 0:
            print(counter, solutioncounter)
        if makespan(rnd) < currentbest:
            currentbest = makespan(rnd)
            pretty_print_solution(rnd)


def mutate(do):
    while True:
        giver = random.choice(people)
        if len(do[giver]) > 0:
            break;
    task = random.choice(do[giver])
    while True:
        receiver = random.choice(people)
        if receiver != giver: break
    reassign_task(do,giver,receiver,task)


def print_gen_data(generation):
    fitness = [makespan(solution) for solution in generation]
    print(f"MIN: {min(fitness)}, AVG: {mean(fitness)}, MAX: {max(fitness)}")
    


def ga(popsize, elit, crossover, mut):
    generation = [ random_solution() for _ in range(popsize)]
    while True:
        print_gen_data(generation)
        generation.sort(key = lambda x : makespan(x))
        new_generation = generation[:elit]
        new_hash = {hash(do) for do in new_generation}
        while len(new_hash) < elit + crossover:
            father=generation[min(random.randrange(popsize), random.randrange(popsize))]
            mother=generation[min(random.randrange(popsize), random.randrange(popsize))]
            child = {person: [] for person in people}
            for task in tasks[:len(tasks)//2]:
                for person in people:
                    if task in father[person]:
                        child[person].append(task)
                        continue
            for task in tasks[len(tasks)//2:]:
                for person in people:
                    if task in mother[person]:
                        child[person].append(task)
                        continue
            mutate(child)
            if hash(child) not in new_hash:
                new_generation.append(child)
                new_hash.add(hash(child))
        while len(new_hash) < elit+crossover+mut:
            selected=generation[min(random.randrange(popsize), random.randrange(popsize))]
            mutated = {
                person : selected[person][:]
                for person in people
            }
            mutate(mutated)
            if hash(mutated) not in new_hash:
                new_generation.append(mutated)
                new_hash.add(hash(mutated))
        while len(new_hash) < popsize:
            rnd = random_solution()
            if hash(rnd) not in new_hash:
                new_generation.append(rnd)
                new_hash.add(hash(rnd))
        generation = new_generation

#iterative_local_search()            
ga(200, 30, 100, 30)