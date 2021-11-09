time = input("Add meg az idot hh:mm:ss formatumban: ")

timelist = time.split(":")

h = int(timelist[0])
m = int(timelist[1])
s = int(timelist[2])

print("Ejfel ota",h*3600+m*60+s,"masodpeerc telt el.")
