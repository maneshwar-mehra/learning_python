# def greet(): # naming the function
#     print("Hi, Good morning")

# greet() # calling or invoking the function


# def randomfunc():
#     print(20)

# x = randomfunc()
# print(x)

# def func2():
#     return 22
# print(func2())

# def three_value_func(value1, value2, value3):
#     print(value1, value2, value3)

# # we can direclty call the function without storing it in a variable. As we are printing something
# # in the function, we just have to provide the value and it will get printed
# three_value_func("I am string", 30, 22.00)


# def iterate_name(name):
#     for i in range(0, len(name)):
#         print(name[i])

# iterate_name("maneshwar")



# taking multiple return statements from a function and storing them in multiple variables
# def random_func(a, b):
#     add = a + b
#     sub = a - b
#     mult = a * b

#     return add, sub, mult

# x, y, z = random_func(10, 5)

# print(x, y, z)

# Question: Create a function in Python
# Write a program to create a function that takes two arguments, name and age, and print their value.
# def name_age(name, age):
#     print(name, age) 

# name_age("mane", 20)




# Write a program to create function such that it can accept two variables and calculate addition and subtraction.
# Also, it must return both addition and subtraction in a single return call.

# def func(a, b):
#     sum = a + b
#     sub = a - b
#     return sum, sub

# result = func(50, 10)
# print(result)



# default argument
# def show_employee(name, salary= 10000): # default argument
#     print(name, salary)


# show_employee("mane", 90000)
# show_employee("alex" ) # if we don't provide any parameter then it will take the default assigned argument


