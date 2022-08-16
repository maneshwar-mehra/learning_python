# how to make an array
# a = [] or a = list(), a =[1,2,3,4,5,6]


# making of a array

company = ["samsung", "tesla", "airtel", "apple"] 
# adding / appending the values to it
company.append("reliance")
print(company)

fruits = ["banana", "mango", "litchi"]
vegetables = ["potato", "tomato", "carrot"]
# adding / extending an array into another array
fruits.extend(vegetables)
print(fruits)


colors = ["red", "blue", "green", "black", "white"]
# .pop removes the item from the list. It takes index as the parameter
colors.pop(1)
print(colors)

clothes = ["jacket", "jeans", "coat", "shirt", "t-shirt"]
# by default it removes the last item from the list
clothes.pop()
print(clothes)



# list comprehension

# simple syntax without list comprehension
# both of the output will be same
a = []
for i in range (0,11):
    a.append (i + 5)
print(a)

# same syntax with list comprehension
# both of the output will be same
b = [i + 5 for i in range(0, 11)]
print(b)

# we can add conditons also
c=[i * 2 for i in range(0, 11) if i > 3]
print(c)



