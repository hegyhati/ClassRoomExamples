time = input("Mennyi az ido? hh:mm:ss formatumban: ")

hm_colon_index = time.find(":")
ms_colon_index = time.find(":", hm_colon_index+1)

h = int(time[:hm_colon_index])
m = int(time[hm_colon_index+1:ms_colon_index])
s = int(time[ms_colon_index+1:])

print("Ejfel ota ", 3600*h+60*m+s, "masodperc telt el.")
