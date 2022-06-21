import random
import tkinter
from logiface import Exercise, Solution

class RandomSolver(tkinter.Tk):

    def __init__(self) -> None:
        super().__init__()
        self.title("Random Solver")
        
        self.exercise = Exercise('exercises/small_triangle.json', 'sets/nine.json')
        self.fitness = tkinter.StringVar()
        tkinter.Label(self,textvar=self.fitness).pack()
        tkinter.Button(self, text="Next", command=self._new_solution).pack()
        tkinter.Button(self, text="Yeppeee", command=self._solve).pack()
        self.canvas = tkinter.Canvas(self,width=self.exercise.width, height=self.exercise.height)
        self._new_solution()
        self.canvas.pack() 
    
        
    def _new_solution(self):
        self.canvas.delete("all")
        self.solution = Solution(self.exercise)
        self.solution.draw(self.canvas)
        self.fitness.set(str(self.solution.fitness()))
    
    def _solve(self):
        while int(self.fitness.get()) != 0:
            self._new_solution()
            self.update()

class LocalSearchSolver(tkinter.Tk):

    def __init__(self) -> None:
        super().__init__()
        self.title("Local Search Solver")
        
        self.exercise = Exercise('exercises/triangle.json', 'sets/nine.json')
        self.fitness = tkinter.StringVar()
        tkinter.Label(self,textvar=self.fitness).pack()
        tkinter.Button(self, text="Random", command=self._new_solution).pack()
        tkinter.Button(self, text="Improve", command=self._improve).pack()
        tkinter.Button(self, text="Yeppeee", command=self._greedy_improve).pack()
        tkinter.Button(self, text="YEPPEEE", command=self._solve).pack()
        self.canvas = tkinter.Canvas(self,width=self.exercise.width, height=self.exercise.height)
        self._new_solution()
        self.canvas.pack() 
    
        
    def _new_solution(self):
        self.solution = Solution(self.exercise)
        self._update_canvas()
    
    def _update_canvas(self):
        self.canvas.delete("all")
        self.solution.draw(self.canvas)
        self.fitness.set(str(self.solution.fitness()))

    
    def _improve(self):
        if self.solution.improve():
            self._update_canvas()
            return True
        return False
        
        

    def _greedy_improve(self):
        while self._improve():
            self.update()
    
    def _solve(self):
        while int(self.fitness.get()) != 0:
            self._new_solution()
            self._greedy_improve()


class GeneticSolver(tkinter.Tk):

    def __init__(self) -> None:
        super().__init__()
        self.title("Genetic Solver")        
        self.exercise = Exercise('exercises/triangle.json', 'sets/nine.json')
        self._init_config()
    
    def _init_config(self):
        self.config_frame = tkinter.Frame(self)
        self.config={}
        configs = {"population_size" : 200, "mutation_count": 80, "crossover_count":150, "elitism_count": 80}
        row = 0
        for conf in configs:
            tkinter.Label(self.config_frame, text=conf).grid(row=row, column=0)
            self.config[conf] = tkinter.IntVar(value=configs[conf])
            tkinter.Entry(self.config_frame, textvariable=self.config[conf]).grid(row=row, column=1)
            row += 1
        tkinter.Button(self.config_frame,text="Yeppeee", command=self._solve).grid(row=row, column=1)
        self.config_frame.pack()
    
    def _init_monitor(self):
        self.monitor_frame = tkinter.Frame(self)
        self.report = tkinter.StringVar()
        self.best = tkinter.Canvas(self.monitor_frame,width=self.exercise.width, height=self.exercise.height)
        self.chart = tkinter.Canvas(self.monitor_frame,width=1000, height=300)
        self.bar_width = 1000 // int(self.config["population_size"].get())
        self.fitness_scale = 5 # magic constant
        self.best.pack()
        tkinter.Label(self.monitor_frame, textvariable=self.report).pack()
        self.chart.pack()
        self.monitor_frame.pack()
    
    def _update_monitor(self):
        best = self.population[0]
        self.best.delete("all")
        self.chart.delete("all")
        self.report.set(f"Iteration: {self.generation}, Best: {best.fitness()}")
        best.draw(self.best)
        self._draw_chart()
        self.update()
    
    def _draw_chart(self):
        for idx, sol in enumerate(self.population):
            self.chart.create_rectangle(idx*self.bar_width, 0, (idx+1)*self.bar_width, sol.fitness() * self.fitness_scale, fill="green")
        

        
    def _generate_initial_population(self):
        self.population = [ Solution(self.exercise) for _ in range(self.config["population_size"].get())]
        self.population.sort(key=lambda x: x.fitness())
    
    def _get_random_solution(self):
        idx = min(random.randrange(self.config["population_size"].get()) for _ in range(2))
        return self.population[idx]
    
    def _generate_new_population(self):
        new_pop = set(self.population[:self.config["elitism_count"].get()])
        for _ in range(self.config["mutation_count"].get()):
            new_pop.add(self._get_random_solution().get_mutated())
        for _ in range(self.config["crossover_count"].get()):
            new_pop.add(Solution.crossover(self._get_random_solution(), self._get_random_solution()))
        while len(new_pop) < self.config["population_size"].get():
            new_pop.add(Solution(self.exercise))
        new_pop = list(new_pop)
        new_pop.sort(key=lambda x: x.fitness())
        new_pop = new_pop[:self.config["population_size"].get()]
        self.population = new_pop
        self.generation += 1
   
    def _solve(self):
        self.config_frame.pack_forget()
        self.generation = 0
        self._generate_initial_population()
        self._init_monitor()
        self._update_monitor()
        while self.population[0].fitness() != 0:
            self._generate_new_population()
            self._update_monitor()

            
                
        


if __name__ == "__main__":
    # RandomSolver().mainloop()
    # LocalSearchSolver().mainloop()
    GeneticSolver().mainloop()