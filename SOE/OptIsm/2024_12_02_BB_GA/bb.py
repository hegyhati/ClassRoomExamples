import problem


solution_sets:set[problem.Solution] = set()
solution_sets.add(problem.all_solutions())

best_value = INFINITY
best_solution = None

while len(solution_sets) != 0:
    current:problem.Solution = solution_sets.pop() # Strategy
    current_objective_value = current.bound() # = current.get_objective()
    if current_objective_value > best_value:
         continue
    if current.is_single_solution():
        best_solution = current
        best_value =  current_objective_value
    else:
        children:set[problem.Solution] = current.branch()
        solution_sets.update(children)

