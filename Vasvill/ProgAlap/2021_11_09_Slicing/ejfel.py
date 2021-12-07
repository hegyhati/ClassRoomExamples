time = input("Kerlek add meg az idot hh:mm formatumban: ")

hours = int(time[:2])
minutes = int(time[-2:])

sincemidnight = hours * 60 + minutes

print("Ejfel ota eltelt percek szama: ", sincemidnight)

print("Ejfel ota eltelt percek szama: ", int(time[:2]) * 60 + int(time[-2:]))
