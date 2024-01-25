import random


puzzles = [
    "May the force be with you.",
    "I'll be back!",
    "Roads? Where we are going, we don't need roads!",
    "My cabbages!!!",
    "Hakuna Matata",
    "I am the night.",
    "I double dare you!",
    "My mama always said, ‘Life was like a box of chocolates. You never know what you’re gonna get.",
    "Clearly, fame is not everything... is it, Mr. Potter?",
    "You can do it!"
]

for i in range(len(puzzles)):
    my_file=open("tests/{}.in".format(i),"wt")
    my_file.write(puzzles[i]+"\n")
    my_file.write("{}\n".format(random.randint(5,20)))
    for j in range(150):
        my_file.write("{}\n".format(chr(random.randint(65,90)+32*random.randint(0,1))))
    my_file.close()    


