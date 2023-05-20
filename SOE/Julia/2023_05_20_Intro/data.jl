using JSON
using Plots

list_jsons() = [file for file in readdir() if file[end-4:end] == ".json" ]

println("Ezek a json file-ok vannak:")
files = list_jsons()
for file in files
    println(" - $file")
end

println("Melyiket akarod megnyitni?")
file = readline()

data = JSON.parsefile(file)
println(data)

for person in data
    println("$(person["name"]) faradtsaga: $(person["tiredness"])")
end

names = [person["name"] for person in data]
tirednesses = [person["tiredness"] for person in data]



p = Plots.bar(names, tirednesses,legend=false, title="Tiredness chart")
Plots.bar!(p,names, [1,1,1])
Plots.savefig(p, "tiredness.png")


