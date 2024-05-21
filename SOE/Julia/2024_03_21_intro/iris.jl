using DataFrames
using CSV
using Plots

df = DataFrame(CSV.File("iris_extended.csv"))

types = ["setosa", "virginica", "versicolor" ]

p = plot()

for type in types
    dff = filter( x -> x.species == type, df )
    plot!(p, dff[!,"sepal_length"], dff[!,"petal_length"], seriestype=:scatter, label=type)
end

savefig(p, "iris.png")
