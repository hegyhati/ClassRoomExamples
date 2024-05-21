using Plots

print("Hany tesztet vegezzek? ")
c = parse(Int,readline())

print("Hany dobas osszeget nezzem? ")
d = parse(Int,readline())

min = d
max = 6*d

tests = [ sum(rand(1:6, d)) for _ in 1:c]
stats = Dict( x => count(==(x),tests) for x in min:max )

p = bar(collect(keys(stats)),collect(values(stats)))
savefig(p, "dice.png")

println(stats)