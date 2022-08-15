arr1 = [5,8,4,6,1,2,7,8] # total index = 7

# gives the whole list
print(arr1[:])

# it's like range just the semicolon difference | will print from starting idx till idx -1
print(arr1[2:5])

# with step: it's like range just the semicolon difference | will print from starting idx till idx -1, with the given step
print(arr1[2:7:2])

# with negative step: it's like range just the semicolon difference | will print from starting idx till idx -1, with the given negative step
print(arr1[7:1:-2])

# to reverse the array
print(arr1[::-1])

# prints everything after the given index, including the given index also
print(arr1[3:])

# print everthing from start till the given index-1
print(arr1[:5])


# we can also use multiple slicing methods for a single array

# this will first print everything till given index-1 and then reverse it 
print(arr1[:6][::-1])
