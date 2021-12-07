time = input("Add meg az idot hh:mm:ss formatumban: ")

if len(time)==8:
    h = int(time[:2])
    m = int(time[3:5])
    s = int(time[-2:])
else: 
    h = int(time[:1])
    m = int(time[2:4])
    s = int(time[-2:])


print("Ejfel ota",h*3600+m*60+s,"masodpeerc telt el.")


