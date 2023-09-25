from timeit import timeit

n = 10**7
print(timeit("tmp=t[1]; t[0]=t[1]; t[1]=tmp", setup = "t=[1,2]", number = n))
print(timeit("t[1],t[0]=t[0],t[1]", setup = "t=[1,2]", number = n))