# tuple -> tuples are immutable, means we cannot change them once assigned
# list -> list is mutable, means we can change them once assigned

# how to make a tuple 
a = ()
print(type(a))

# if we want to make a tuple with single value we have to put comma (,) after the value
b = ("apple",)
print(type(b))

# tuple with multiple values
c = ("apple", "banana", "cherry")
print(c)

# tuple will not have append, extend and pop
# we cannot update values in tuple
# tuple will have slicing and indexing

d =("red", "black", "white")
print(d[0])
# we cannot update the values once assigned
d[0] = "yellow"

