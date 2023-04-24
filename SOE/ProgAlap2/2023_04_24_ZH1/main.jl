using JSON
using Plots

function result_plot(subject::String, year::Integer) 
    data = JSON.parsefile("results/$(year)/$(subject).json")
    grades = values(data)
    grade_options = [1,2,3,4,5]
    count_options = [count(x -> (x==grade), grades) for grade in grade_options]
    Plots.savefig(Plots.bar(grade_options, count_options,legend = false, title="$subject results in $year"), "$(subject)_$(year)_results_jl.png")
end

result_plot("math",2020)

function percentage(subject::String, year::String) :: Real 
    try
        data = JSON.parsefile("results/$(year)/$(subject).json")
        pass = count(x -> (x>1), values(data))
        pass / length(data)
    catch
        return 0
    end
end

function result_plot_over_years(subjects::Array{String})
    years = readdir("results")
    p = Plots.plot(title="Pass statistics for " * join(subjects," "))
    for subject in subjects
        percentages = [percentage(subject,year) for year in years]
        Plots.plot!(p, years,percentages, label=subject)
    end    
    Plots.savefig(p, join(subjects,"_") * "_results_jl.png")
    
end

result_plot_over_years(["math","music"])