def increase(a):
    a += 1

def append_one(mylist):
    mylist.append(1)

def reset(mylist):
    mylist = []

x = 2
increase(2*x)
print(x)

l = [2,3]
append_one(l)
print(l)
reset(l)
print(l)