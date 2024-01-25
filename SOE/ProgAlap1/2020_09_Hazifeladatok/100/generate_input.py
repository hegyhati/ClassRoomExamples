import random
import solution
import pickle


for testcase in range(1,20):
    total_distance=random.uniform(6000,32000)
    start_time=random.randint(0,10000)
    gpx=[{"position":(0,0),"elavation":0,"timestamp":start_time}]
    while solution.total_distance(gpx)<total_distance:
        speed=random.uniform(9,13)
        for i in range(random.randint(30,200)):
            time=random.randint(1,4)
            distance=speed * 1000 * time / 3600
            dx=random.uniform(0,distance)
            dy=(distance**2-dx**2)**0.5
            if(random.random()>0.7): dx*=-1
            if(random.random()>0.9): dy*=-1    
            if(random.random()<0.05): dx=dy=0
            new_position=(gpx[-1]["position"][0]+dx,gpx[-1]["position"][0]+dy)
            new_elavation=gpx[-1]["elavation"]+random.uniform(-0.1,0.3)
            new_timestamp=gpx[-1]["timestamp"]+time
            gpx.append({"position":new_position,"elavation":new_elavation,"timestamp":new_timestamp})

    my_data_file=open(f"tests/test{testcase}.pickle","wb")
    pickle.dump(gpx,my_data_file)
    my_data_file.close()
    my_file=open(f"tests/test{testcase}.in","wt")
    my_file.write(f"tests/test{testcase}.pickle\n")
    my_file.close()

