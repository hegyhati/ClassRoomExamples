n = int(input("Hány csapat van a bajnokságban? "))
print("Nem lesz meccs." if n==1 else f"{n*(n-1)//2} meccs lesz.")