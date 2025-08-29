time = input("Add meg az idot hh:mm:ss formatumban: ")

[h,m,s]= [int(x) for x in time.split(":")]

print("Ejfel ota",h*3600+m*60+s,"masodpeerc telt el.")
