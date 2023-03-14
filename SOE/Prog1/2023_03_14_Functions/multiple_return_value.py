def gcd_scm(number1, number2):
    for maybe_divider in range(number1,0,-1):
        if number1 % maybe_divider == 0 and number2 % maybe_divider == 0:
            return maybe_divider , number1 * number2 // maybe_divider

    

n1 = int(input())
n2 = int(input())
a,b = gcd_scm(n1,n2)

print(a,b)