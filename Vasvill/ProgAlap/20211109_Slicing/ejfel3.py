time = input("Add meg az idot hh:mm:ss formatumban: ")

h = int(time[:-6])
m = int(time[-5:-3])
s = int(time[-2:])

print("Ejfel ota",h*3600+m*60+s,"masodpeerc telt el.")
