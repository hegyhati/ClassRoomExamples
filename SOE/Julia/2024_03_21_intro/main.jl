using PyCall

py"""
def foo(x):
    return 2**x
"""

for a in 1:10
    println(py"foo"(a))
end

l = Vector{UInt16}([1,2,3])