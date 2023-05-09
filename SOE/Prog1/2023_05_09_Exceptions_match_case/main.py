def safe_user_input_number():
    while True:
        try:
            x = int(input())
            break
        except Exception:
            print("You need to give a number.")
    return x


x = safe_user_input_number()
y = safe_user_input_number()
print( x+y )
