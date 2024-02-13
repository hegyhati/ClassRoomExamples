problem = input("Do you have a problem? (yes/no) ")
if problem == "no":
    # nincs problemam
    print("Then you have nothing to worry about.")
else:
    # van valami gubanc
    cando = input("Can you do something about it? (yes/no) ")
    if cando == "yes" :
        print("Then do it.")
    else:
        print("Then you should not worry about it.")
