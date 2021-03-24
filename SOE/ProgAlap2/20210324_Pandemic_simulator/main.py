import matplotlib.pyplot as plt
from virus import *
import random
import os


count = 100
width=4000
height=3000
intial_infected=5
time_length=400

area = Area(width,height)


people = []

for _ in range(count):
    people.append(Person( area, (random.randint(0,width), random.randint(0,height)), (random.randint(0,30),random.randint(0,30)) ))

for i in range(intial_infected):
    people[i].infect()


fig,axes=plt.subplots()

fig2,axes2=plt.subplots()
timeinterval=list(range(time_length))
endangered=[]
infected=[]

for time in range(time_length):
    x=[]
    y=[]
    color=[]
    infected_count=0
    recovered_count=0
    for person in people:
        person.move()
        x.append(person.position[0])
        y.append(person.position[1])
        color.append("red" if person.is_infected() else "gray" if person.is_recovered() else "green")
        if person.is_infected(): 
            infected_count+=1
        elif person.is_recovered(): 
            recovered_count+=1
    infected.append(100 * infected_count / count)
    endangered.append(100 - 100 * recovered_count / count)
    
    for p1 in people:
        for p2 in people:
            if p1!=p2:
                if p1.distance_from(p2) < 50 and p1.is_infected():
                    p2.infect()
    axes.cla()
    axes.set_xlim(0,width)
    axes.set_ylim(0,height)
    axes.scatter(x,y, c=color)
    fig.savefig('timeline/{:05}.png'.format(time))

bottom=[0] * time_length
top=[100]*time_length
axes2.fill_between(timeinterval, bottom, infected, color="red")
axes2.fill_between(timeinterval, infected, endangered, color="green")
axes2.fill_between(timeinterval, endangered, top, color="gray")
fig2.savefig('timeline.png')

os.system("ffmpeg -framerate 20 -i timeline/%05d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p output.mp4")

