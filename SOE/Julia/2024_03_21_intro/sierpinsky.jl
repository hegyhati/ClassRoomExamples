factorial(n) =  n == 0 ? 1 : n * factorial(n-1)
binom(n,k) = factorial(n) ÷ factorial(k) ÷ factorial(n-k)


function print_pascal_triangle(depth)
    for r in 0:depth-1
        print(" " ^ (depth-r))
        for c in 0:r 
            print(binom(r,c), " ")
        end
        println()
    end
end

function print_sierpinsky_triangle(depth)
    for r in 0:depth-1
        print(" " ^ (depth-r))
        for c in 0:r 
            print( binom(r,c) % 2 == 1 ? "XX" : "  ")
        end
        println()
    end
end

print_sierpinsky_triangle(33)