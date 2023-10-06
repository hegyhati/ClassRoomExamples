from threading import Thread
from time import sleep

def foo():
    print("Foo starts...")
    # doing some serious background work
    sleep(3)
    print("Foo done")


foo_thread = Thread(target=foo)
foo_thread.start()

print("Work that is not dependent on foo.")

foo_thread.join() # Wait for foo_thread to end
print("Work that requires that foo is finished.")
