from random import randint

data = [str(randint(1,100)) for _ in range(randint(1000,2000))]

with open("test.txt", "w") as f:
    f.write(', '.join(data) + '\n')
