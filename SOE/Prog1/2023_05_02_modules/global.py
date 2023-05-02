def foo():
    global x
    x = 4
    print(f"foo : {x}")

x = 3
foo()
print(f"global: {x}")
