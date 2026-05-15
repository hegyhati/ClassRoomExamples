import random

count = random.randint(5,10)

with open("intersection.txt","w") as f:
    f.write(f"{count}\n")
    for id in range(count):
        f.write(f"I{id:02} Cars: {random.randint(10,100)} Bikes: {random.randint(0,50)} Pedestrians: {random.randint(100,200)}\n")
    
    for a,b in (tuple(s) for s in {
        frozenset(random.sample(range(count), k=2))
        for _ in range (random.randint(2*count, 5*count))
    }) : f.write(f"I{a:02} - I{b:02} : {random.uniform(1,10):.3} km\n")
         
                                