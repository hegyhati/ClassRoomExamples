from functools import partial

def multiple_print(count: int, text:str):
    for _ in range(count):
        print(text)


multiple_print(5, "hello")

sokszia = partial(multiple_print, text="szia")
sokszia(5)
sokhello = partial(multiple_print, text="hellobello")
sokhello(10)


doubleprint = partial(multiple_print, count=2)
doubleprint(text="Double")
