points = ["vertex indices in obj files start at 1...."]
triangles = []

with open("bunny.obj") as f:
    for line in f:
        match line.strip().split(" "):
            case ["v", "", x,y,z]: points.append((float(x), float(y), float(z)))
            case ["f", x,y,z]: 
                triangles.append((
                points[int(x.split("/")[0])],
                points[int(y.split("/")[0])],
                points[int(z.split("/")[0])],
            ))
with open("bunny.txt", "w") as f:
    f.write(f"{len(triangles)}\n")
    for t in triangles:
        for p in t:
            for c in p:
                f.write(f"{c:.6f} ")
        f.write("\n")

                                             
                                             

