import os
import matplotlib.pyplot as plt


class TrainingStep:
  def __init__(self, name:str, duration_in_seconds:int, hr_lower_limit:int, hr_upper_limit:int):
    if duration_in_seconds < 0 or hr_lower_limit > hr_upper_limit or hr_lower_limit < 40 or hr_upper_limit > 210:
      raise Exception
    self._name = name
    self._duration = duration_in_seconds
    self._hr_zone = (hr_lower_limit, hr_upper_limit)

class Training:
  
  def __init__(self):
    self.__steps = []

  def add_step(self, name:str, duration_in_seconds:int, hr_lower_limit:int, hr_upper_limit:int) -> None:
    try:
      self.__steps.append(TrainingStep(name,duration_in_seconds,hr_lower_limit,hr_upper_limit))
    except Exception:
      print("Could not add step, invalid data provided.")
  
  def repeat(self, step_count:int, repeat_count:int) -> None:
    if step_count > len(self.__steps) or step_count <= 0 or repeat_count <= 0:
      print("Could not repeat steps, invalid arguments.")
    else:
      for _ in range(repeat_count):
        self.__steps.extend(self.__steps[-step_count:])
  
  def print(self) -> None:
    for step in self.__steps:
      print("{0._name:>20} ({0._duration:>4} s): {0._hr_zone[0]}-{0._hr_zone[1]} bpm".format(step))

  def total_time(self) -> int:
    sum=0
    for step in self.__steps:
      sum += step._duration
    return sum
  
  def get_zone(self, time_in_seconds:int) -> tuple:
    if time_in_seconds < 0 or time_in_seconds >= self.total_time(): return None
    for step in self.__steps:
      time_in_seconds -= step._duration
      if time_in_seconds < 0: return step._hr_zone

  def __extract_hr(self,filename:str) -> list:
    hr_data = []
    with open(filename,"rt") as hr_file:
      for hr in hr_file:
        hr_data.append(int(hr))
    return hr_data

  def __plot(self, real_hr:list, filename:str) -> None:
    f,a = plt.subplots()
    time = list(range(self.total_time()))
    lower=[]
    upper=[]
    for step in self.__steps:
      lower.extend([step._hr_zone[0]]*step._duration)
      upper.extend([step._hr_zone[1]]*step._duration)
    a.fill_between(time,lower,upper, color="green")
    a.plot(time,real_hr[:self.total_time()], color="red")
    a.set_xlabel("time (s)")
    a.set_ylabel("HR (bpm)")
    a.set_title("HR diagram")
    f.savefig(filename)

  def __good_percentage(self,real_hr:list) -> int:
    good = 0
    for time in range(self.total_time()):
      lower,upper = self.get_zone(time)
      if real_hr[time] >= lower and real_hr[time]<=upper: good+=1 
    return int(100*good/self.total_time())

      
    
  def examine(self,filename:str) -> int:
    if not os.path.isfile(filename): 
      print("Wrong filename.")
      return None
    real_hr = self.__extract_hr(filename)
    outfile = os.path.splitext(filename)[0]+".png"
    self.__plot(real_hr,outfile)
    return self.__good_percentage(real_hr)
    
        


