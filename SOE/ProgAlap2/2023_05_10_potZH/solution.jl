using Plots
using Statistics

function count_word(filename::String, word::String) :: Integer
    open(filename) do f
        return count(==(lowercase(word)), split(lowercase(read(f, String))))
    end
end

function search(word::String)
    data = Dict(
        site => sum(
            [count_word("articles/$(site)/$(article)", word) for article in readdir("articles/$(site)") ]
        )
        for site in readdir("articles")
    )
    Plots.savefig(
        Plots.bar( [keys(data)...],[values(data)...], title="Talalatok \"$word\"-re", legend=false),
        "$(word)_jl.png"
    )
end


function average_word_length(article_path::String, min_length::Integer) :: AbstractFloat
    open(article_path) do f
        return mean([length(word) for word in split(read(f, String)) if length(word)>=min_length])
    end
end

function website_average_word_statistics(sites::Array{String}, min_length::Integer = 5)
    p = Plots.plot(title = "$(join(sites,", ")) szohossz atlagok")
    for site in sites
        Plots.plot!(p, [average_word_length("articles/$site/$article",min_length) for article in sort(readdir("articles/$site/"))], label = site)
    end
    Plots.savefig(p,"$(join(sites,"_"))_jl.png")
end

search("egY")
website_average_word_statistics(["hvg","index","origo"])

