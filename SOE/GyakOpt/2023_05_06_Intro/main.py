

import random

from matplotlib import pyplot as plt


people = []
hours = []
filename = "tasks.csv"

maybe_optimal = ["Erno", "Balazs", "Balazs", "Julcsi", "Julcsi", "Erno", "Erno", "Balazs", "Balazs",
                 "Balazs", "Julcsi", "Erno", "Balazs", "Erno", "Julcsi", "Julcsi", "Erno", "Julcsi", "Erno", "Erno"]


def load_data(filename):
    global people
    global hours
    with open(filename) as f:
        people = [name.strip() for name in f.readline().split(",")]
        for line in f:
            items = [name.strip() for name in line.split(",")]
            hours.append({people[i]: float(items[i+1])
                         for i in range(len(people))})


def random_solution():
    return tuple([random.choice(people) for _ in range(len(hours))])


def fitness(solution):
    sum = {person: 0 for person in people}
    for i in range(len(hours)):
        sum[solution[i]] += hours[i][solution[i]]
    return max(sum.values())

def fitness2(solution):
    sum = 0
    for i in range(len(hours)):
        sum += hours[i][solution[i]]
    return sum

def improve_solution_by_move(solution) -> bool: # todo modify for tuples
    original_value = fitness(solution)
    for job in range(len(hours)):
        original_person = solution[job]
        for person in people:
            solution[job] = person
            if fitness(solution) < original_value:
                return True
        solution[job] = original_person
    return False


def improve_solution_by_swap(solution) -> bool: # todo modify for tuples
    original_value = fitness(solution)
    for job1 in range(len(hours)):
        for job2 in range(job1+1, len(hours)):
            solution[job1], solution[job2] = solution[job2], solution[job1]
            if fitness(solution) < original_value:
                return True
            solution[job1], solution[job2] = solution[job2], solution[job1]
    return False


def iterative_local_search():  # todo modify for tuples
    best = 1000
    while True:
        solution = random_solution()
        while improve_solution_by_swap(solution):
            pass
        print(best, fitness(solution))

        if fitness(solution) < best:
            best = fitness(solution)


load_data(filename)


def genetic_algotithm():
    population_size = 200
    elitism = 20
    mutation = 80
    crossover_count = 150
    generations = 200000


    def select_solution(population):
        selected = min([random.randrange(population_size) for _ in range(2)])
        return population[selected]


    def mutate(solution):
        job1 = random.randrange(len(hours))
        job2 = random.randrange(len(hours))
        new_solution = list(solution)
        new_solution[job1], new_solution[job2] = new_solution[job2], new_solution[job1]
        return tuple(new_solution)


    def crossover(solution1, solution2):
        pivot = random.randrange(population_size)
        return tuple(solution1[:pivot] + solution2[pivot:])
    
    current_population = [random_solution() for _ in range(population_size)]
    current_population.sort(key=fitness)

    for _ in range(generations):
        print(_, [fitness(solution) for solution in current_population[:6]])
        new_population = current_population[:elitism]
        for _ in range(mutation):
            solution = select_solution(current_population)
            new_population.append(mutate(solution))
        for _ in range(crossover_count):
            solution1 = select_solution(current_population)
            solution2 = select_solution(current_population)
            new_population.append(crossover(solution1, solution2))
        new_population = set(new_population)
        while len(new_population) < population_size:
            new_population.add(random_solution())
        new_population = list(new_population)
        new_population.sort(key=fitness)
        new_population = new_population[:population_size]
        current_population = new_population


def multiobjective_plot(count):
    x = []
    y = []
    for _ in range(count):
        solution = random_solution()
        x.append(fitness(solution))
        y.append(fitness2(solution))
    fig,ax = plt.subplots()
    ax.scatter(x, y)

    for idx1 in range(count-1,-1,-1):
        for idx2 in range(len(x)):
            if x[idx2] < x[idx1] and y[idx2] < y[idx1]:
                del x[idx1]
                del y[idx1]
                break
    ax.scatter(x,y)        


    fig.savefig("ize.png")

multiobjective_plot(50000)
