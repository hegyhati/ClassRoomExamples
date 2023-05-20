using PyCall

depth = parse(Int, readline())

# function fact(n)
#     result = 1
#     for i in 1:n
#         result *= i
#     end
#     return result
# end

py"""
def fact(n):
    return 1 if n==0  else n*fact(n-1)
"""


# function binom(n,k)
#     return div(fact(n),  fact(k) * fact(n-k))
# end

# function binom(n,k)
#     div(fact(n),  fact(k) * fact(n-k))
# end

binom(n,k) = div(py"fact"(n),  py"fact"(k) * py"fact"(n-k))

for d in 0:depth
    for c in 0:d
        print(binom(d,c))
    end
    println()
end
