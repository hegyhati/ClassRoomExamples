from copy import deepcopy
import random
import json

with open("data.json") as f:
    data = json.load(f)

supplies = list(data["Supplies"].keys())
demands = list(data["Demands"].keys())
totaldemand = sum(data["Demands"][d] for d in demands)

def get_random_solution() -> dict[str,dict[str,float]]:
    return {
        s : {
            d : random.randrange(2 * totaldemand // len(supplies) // len(demands)) for d in demands
        } for s in supplies
    }

def get_zero_solution() -> dict[str,dict[str,float]]:
    return {
        s : {
            d : 0 for d in demands
        } for s in supplies
    }

def transport_cost(solution)->float:
    sum = 0
    for s in supplies:
        for d in demands:
            sum += solution[s][d] * data["Distances"][s][d]
    return sum
    
def removed(solution, s):
    sum = 0
    for demand, qty in solution[s].items():
        sum += qty
    return sum

def supplied(solution, d):
    sum = 0   
    for s, demands in solution.items():
        sum += demands[d]
    return sum


PENALTY = 1000
def penalty_cost(solution) -> float:
    penalty = 0
    for s in supplies:
        penalty += PENALTY * (removed(solution, s) - data["Supplies"][s])**2
    for d in demands:
        penalty += PENALTY * (data["Demands"][d] - supplied(solution, d))**2
    for s in supplies:
        for d in demands:
            if solution[s][d] < 0:
                penalty += PENALTY * solution[s][d]**2
    return penalty



def fitness(solution:dict[str,dict[str,float]]) -> float:
    return transport_cost(solution) + penalty_cost(solution)


MUTATION_SIZE = 200
MUTATION_SIZE_SCALE = 0.8
MUTATION_DECREASE_CYCLE = 50


def get_transport():
    return random.choice(supplies), random.choice(demands)

def mutate_single_change(solution):
    amount = random.randrange(-MUTATION_SIZE,+MUTATION_SIZE)
    s,d = get_transport()
    solution[s][d] -= amount
    
def mutate_single_move(solution):
    amount = random.randrange(-MUTATION_SIZE,+MUTATION_SIZE)
    s1,d1 = get_transport()
    s2,d2 = get_transport()
    solution[s1][d1] -= amount
    solution[s2][d2] += amount
    
def mutate_shift(solution):
    amount = random.randrange(-MUTATION_SIZE,+MUTATION_SIZE)
    s1,d1 = get_transport()
    s2,d2 = get_transport()
    solution[s1][d1] -= amount
    solution[s1][d2] += amount
    solution[s2][d2] -= amount
    solution[s2][d1] += amount

def mutate(solution):
    random.choice([mutate_single_change, mutate_single_move, mutate_shift, mutate_shift])(solution)

def crossover(solution1, solution2):
    if random.random() < 0.5:
        first = supplies[:len(supplies)//2]
        return {
            s : deepcopy(solution1[s]) if s in first else deepcopy(solution2[s])
            for s in supplies
        }
    else:
        l = random.random()
        return {
            s: {
                d : int(l*solution1[s][d] + (1-l)*solution2[s][d]) for d in demands
            } for s in supplies
        }


def print_solution(solution):
    print()
    for s in supplies:
        print(s, data["Supplies"][s], removed(solution, s))
    print()
    for d in demands:
        print(d, data["Demands"][d], supplied(solution, d),)



POP_SIZE = 500
ELITE_COUNT = 20
CROSSOVER_COUNT = 200
JUSTMUTATE_COUNT = 275
NEW_RANDOM = 5
MUTATION_RATE = 0.7


population = [ get_random_solution() for _ in range(POP_SIZE)]
population.sort(key= lambda x: fitness(x))


def first_feasible(population):
    for solution in population:
        if penalty_cost(solution) == 0:
            return solution
    return None


generation = 0
while True:
    generation += 1
    print(f"\n\nGeneration {generation}:\nMAX_MUTATE={MUTATION_SIZE}")
    print(f"Fitness: BEST: {fitness(population[0])} MEDIAN: {fitness(population[POP_SIZE//2])}, WORST: {fitness(population[-1])}")
    print()
    best_feasible = first_feasible(population)
    if best_feasible is not None:
        print(f"Fitness of best feasible solution: {fitness(best_feasible)}")
    else:
        print("No feasible, best non-feasible solution:")
        # print_solution(population[0])
    if generation % MUTATION_DECREASE_CYCLE == 0:
        MUTATION_SIZE = max(10, int(MUTATION_SIZE * MUTATION_SIZE_SCALE))
    
    new_population = deepcopy(population[:ELITE_COUNT])
    for _ in range(CROSSOVER_COUNT):
        s1idx = min(random.randrange(POP_SIZE) for _ in range(2))
        s2idx = min(random.randrange(POP_SIZE) for _ in range(6))
        new_population.append(crossover(population[s1idx], population[s2idx]))
        if random.random() < MUTATION_RATE:
            mutate(new_population[-1])
    for _ in range(JUSTMUTATE_COUNT):
        idx = min(random.randrange(POP_SIZE) for _ in range(8))
        new_solution = deepcopy(population[idx])
        mutate(new_solution)
        new_population.append(new_solution)
    for _ in range(NEW_RANDOM):
        new_population.append(get_random_solution())
    population = new_population
    population.sort(key= lambda x: fitness(x))