import random

moves=("left","right","up","down")
for testcase in range(50):
    my_file=open("tests/"+str(testcase)+".in","wt")
    my_file.write(str(random.randint(2,5))+"\n")
    for i in range(random.randint(0,50)):
        move=moves[random.randint(0,3)]
        my_file.write(move + "\n")
    my_file.write("end\n")
    my_file.close()


