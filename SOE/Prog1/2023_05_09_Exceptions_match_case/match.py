x = input().split()

match(x):
    case [single] : print(f"Hello {single}!") 
    case [first, second] : print(f"Hello {first} and {second}!")
    case [*everyone, "Pista"] : print(f"Hello to everyone except Pista, we don't like him.")
    case [first, *others] if "Pista" not in others: print(f"Hello {first} and friends!")
    case _: print("Pista...")
