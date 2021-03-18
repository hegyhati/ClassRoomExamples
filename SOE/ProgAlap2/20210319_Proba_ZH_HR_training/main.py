from training import Training

thursday = Training()

thursday.add_step("Warm up", 300, 144, 151)
thursday.add_step("Wrong timing", -45, 120, 120) #  not added
thursday.add_step("Comfortable run", 1200, 149, 157)
thursday.add_step("Energetic run", 180, 158, 166)
thursday.add_step("Recovery", 120, 146, 153)
thursday.repeat(2, 2) # repeat the last 2 steps 2 times 
thursday.add_step("Intensive run", 180, 167, 175)
thursday.add_step("Recovery", 120, 146, 153)
thursday.add_step("Comfortable run", 900, 149, 157)
thursday.add_step("Cool down", 300, 140, 148)

print()
print("The training:")
thursday.print()

print()
print("Total time: {} s".format(thursday.total_time()))

print()
print("HR zones:")
for time in [0,1234,12345]:
  print(" - At {} s : {}".format(time,thursday.get_zone(time)))


print()
print("Examine none-existent run.txt")
thursday.examine("run.txt")

print()
print("Examine run_hr.txt")
good = thursday.examine("run_hr.txt")
print("{}% of the time the HR zones were met.".format(good))
