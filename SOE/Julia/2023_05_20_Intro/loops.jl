countrolls = parse(Int, readline())

dice = 1:6
dicerolls = rand(dice, countrolls)
statistics = [ count( ==(x), dicerolls) for x in dice ]

for d in dice
    println(" $(d): $(statistics[d])")
end


