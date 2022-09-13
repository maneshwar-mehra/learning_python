# # how to make a dictionary
# # a = {} or a = dict()

# # dictionary are "key": value pairs


# dict1 = {"a": 100, "b":200, "c": 300, "d": 400}
# print(dict1)


# dict2 =  {"w": 100, "x":200, "y": 300, "z": 400}
# print(dict2)
# #  to get a specific values from a dictionary we use "keys" with  "" 
# print(dict2["x"])


# # dictionary are mutable, means we can change the values once assigned
# # "keys" can not be changed only their values can be changed
# dict3 =  {"e": 100, "f":200, "g": 300, "h": 400}
# print(dict3)
# # updating a value
# dict3["g"] = 1000
# print("after updating g", dict3)


# # to add a new key into the dictionary
# dict3["h1"] = 2000
# print("after adding h1", dict3) 


# # we can also put integer as a key
# dict3[10] = 10000
# print("after adding 10 as a key", dict3)


# # deleting a "key": value from a dictionary
# # syntax -> dict3.pop("key")
# dict3.pop("e")
# print("after popping e", dict3)


# # to get all the keys of the dictionary
# print(dict3.keys())
# # if we want to typecast it into a list
# print(list(dict3.keys()))


# # to get all the values of the dictionary
# print(dict3.values())
# # if we want to typecast it into a list
# print(list(dict3.values()))


# # items -> will give an array of tuples in which each tuple will have "key", value
# # something like this -> [("key1", 100), ("key2", 110), ("key3", 101), ("key4", 1000)]
# print(dict3.items())


# # iteration in dictionary
# for key, value in dict3.items():
#     print(key, value)






# some practice questions


# thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

# for i in thisdict:
#     print(i, thisdict[i])



# Create a dictionary whose keys are month names and whose values are
# number of days in the corresponding months.
# a. Ask user to enter month name and number of days.
# b. Print out all of the keys in alphabetical order.
# c. Print out all of the months with 31 days.
# d. Print out the (key-value) pairs sorted by keys.
# e. Print out the (key-value) pairs sorted by values.

# dict1 = {"jan": 31, "feb": 28, "mar": 31, "apr":30, "may": 31, "june": 30,
#             "july": 31, "aug": 31, "sep":30, "oct": 31, "nov": 30, "dec": 31}

# a.
# z = input()
# print(dict1[z])


#  c.
# for i in dict1:
#     if (dict1[i]) == 31:
#         print(i)


dict44 = {}

dict44["apple"] = "company"
dict44["product"] = "iphone"
dict44["type"] = "Smart Phone"


# for keys
# for i in dict44:
#     print(i)


# for values
# for i in dict44:
#     print(dict44[i])


# for keys and values
# for x, y in dict44.items():
#     print(x, y)

print(dict44)