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
        current = int(self.fitness.get())
        for i in range(self.exercise.place_count):
            for r in range(2):
                self.solution.rotate(i)
                if self.solution.fitness() < current:
                    self._update_canvas()
                    return True
            self.solution.rotate(i)
        
        for i in range(self.exercise.place_count):
            for j in range(i+1,self.exercise.place_count):
                cri = self.solution.rotation[i]
                crj = self.solution.rotation[j]
                self.solution.selection[i], self.solution.selection[j] = self.solution.selection[j], self.solution.selection[i]
                for ri in range(3):
                    self.solution.rotation[i] = ri   
                    for rj in range(3):
                        self.solution.rotation[j] = rj
                        if self.solution.fitness() < current:
                            self._update_canvas()
                            return True                
                self.solution.selection[i], self.solution.selection[j] = self.solution.selection[j], self.solution.selection[i]
                self.solution.rotation[i] = cri
                self.solution.rotation[j] = crj


        return False

    def _greedy_improve(self):
        while self._improve():
            self.update()
    
    def _solve(self):
        while int(self.fitness.get()) != 0:
            self._new_solution()
            self._greedy_improve()




if __name__ == "__main__":
    # RandomSolver().mainloop()
    LocalSearchSolver().mainloop()