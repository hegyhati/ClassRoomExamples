import threading

def echo():
    x = input()
    print(x)

t = threading.Thread(target=echo)

t.start()

print('alma')

t.join()

print("korte")
