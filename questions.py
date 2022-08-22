# Write a program to check if a no is even or odd. If its even print even else print odd.

# number = 17

# if(number % 2 == 0):
#     print("Even")
# else:
#     print("odd")

# ####################################################################

    # if False:
    #     print(0)
    # else:
    #     if True or False:
    #         print(1)
    #     elif True and True:
    #         print(2)
    #     if False and False:
    #         print(3)
    #     print(4)

# age = 10
# if True:
#     if age == 10:
#         print(1)
#     else:
#         print(2)
#     if age * 4 > 20:
#         print(3)
#         print(4)
#     elif age * 2 >= 20:
#         print(5)
#         print(6)
#     else:
#         print(7)
# print(8)
# if age == 10:
#     print(9)
#     print(10)
# print(11)

# Program to tell age of the user

# current_year= 2022

# user_born_year= int(input("Please enter your year of birth in numerical "))

# user_age = current_year - user_born_year

# print(user_age)



# Question: print all the number in the range 1-50

# # 1st method
# for i in range(1, 51):
#     if i % 2 == 0:
#         print(i)

# # # 2nd method
# for i in range(2, 51, 2):
#     print(i)

# n = int(input())
# for i in range(1, n):
#     if i % 4 == 0 and i % 3 == 0:
#         print(i, "divisible by both 4 and 3")
#     if i % 3 == 0:
#         print(i, "divisible by 3")
#     if i % 4 == 0:
#         print(i, "divisible by 4")




# Question
# Write a user driven program which will print the tables of a no given by user
# num = int(input())

# for i in range(0, 11):
#     print(num, i, num * i )
#     i +=1



# Question
# Write a program to print vowels in a string given by the user.
# str1 = input()

# for i in str1:
#     if (i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
#         print(i)



# Question
# Write a loop to find the factorial of any number
# i = int(input())
# fact = 1
# while(i > 0):
#     fact= fact*i
#     i=i-1
# print("factorial is", fact)




# Question
# Print First 10 natural numbers using while loop
# nat_number = 0
# while (nat_number <11):
#     print(nat_number)
#     nat_number=nat_number+1


# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# Question
# reverse a string

# def reverse_string(name):
# # len(name) -1,-1,-1 | this means that we are going in reverse till 0th index
# # with a negative -1 step
# # the range now will be -> 8,7,6,5,4,3,2,1,0 
# #                          r a w h s e n a m  
#     for i in range(len(name)-1,-1,-1):
#         print(name[i])

# reverse_string("maneshwar")

# Question
# Write a Python function to find the Max of three numbers

# def maxOfThreeNo(num1, num2, num3):
#     if num1 > num2 and num1 > num3:
#         print(num1)
#     elif num2 > num1 and num2 > num3:
#         print(num2)
#     else:
#         print(num3)

# maxOfThreeNo(100, 1500, 200)



# Question
# Write a program which counts the no of vowels in a string
# def noOfVovels(string):
#     vovel = 0
#     for i in range(0, len(string)):
#         if string[i]!=" ":
#             if(string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or
#             string[i] == "u" or string[i] == "A" or string[i] == "E" or string[i] == "I" or string[i] == "O" or
#             string[i] == "U"):
#                 vovel = vovel+1

#     print(vovel)

# noOfVovels("Mane")




# Question
# Write a program which counts the no of vowels and consonants in a string
# def noOfVovels(string):
#     vovel = 0
#     consonants = 0
#     for i in range(0, len(string)):
#         if string[i]!=" ":
#             if(string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or
#             string[i] == "u" or string[i] == "A" or string[i] == "E" or string[i] == "I" or string[i] == "O" or
#             string[i] == "U"):
#                 vovel = vovel+1
#             else:
#                 consonants = consonants+1
#     print("No of vovel", vovel)
#     print("No of consonants", consonants) 

# noOfVovels("Mane")

# Question
# Write a Python function that takes a number as a parameter and check the
# number is prime or not.
# Note : A prime number (or a prime) is a natural number greater than 1 and that
# has no positive divisors other than 1 and itself

# def primeNo(no):
#     if no > 1 and no%no == 0 and no % 1 == 0:
#         print(no, "is prime number")
#     else:
#         print(no, "is not a prime number")

# primeNo(5)


# Question
# Write a Python program to sum all the items in a list.
# lst1 = [1,2,3,4,5,6]

# sum = 0
# for i in range(0, len(lst1)):
#     sum = sum + lst1[i]
# print(sum)



# Write a Python program to get the largest number from a list
# a = []
# size = int(input("Enter the size of the list "))
# for i in range(size):
#     val = int(input("Please enter your number "))
#     a.append(val)

# max = a[0]
# for i in range (size):
#     if (max < a[i]):
#         max = a[i]
# print("max number is ", max)

# print("your list is ",a)




#  Question
# Write a Python program to round the numbers of a given list, print the minimum
# and maximum numbers and multiply the numbers by 5. Print the unique numbers
# in ascending order separated by space.
# Original list: [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
# Minimum value: 4
# Maximum value: 22
# Result:
# 20 25 45 55 60 70 80 90 110

# original_list= [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]

# for i in range(0, len(original_list)):
#     original_list[i] = int(original_list[i])
# print(original_list)
# # max value
# max_val = original_list[0]
# for i in range(0, len(original_list)):
#     if max_val < original_list[i]:
#         max_val = original_list[i]
# print("max value is", max_val)
# # min value
# min_val = original_list[0]
# for i in range(0, len(original_list)):
#     if original_list[i] < min_val: 
#         min_val = original_list[i]
# print("min value is", min_val)
# # multuply each value by 5
# new_lst = []
# for i in original_list:
#     new_lst.append(i * 5)
# print(new_lst)


# Question from week-4 day-4 lecture video (watch week-4 day-4 lecture video to get the question)

# print("enter the number of students", end=" ")
# no_of_students = int(input())
# print("enter the number of subjects", end=" ")
# no_of_subjects = int(input())

# results_dict = {}
# for i in range(no_of_students):
#     print("enter student name")
#     student_name = input()
#     print("enter the marks of ", student_name)
#     marks = list(map(int, input().split(" "))) [:no_of_subjects]

#     sum_of_all_marks = 0
#     for i in marks:
#         sum_of_all_marks += i

#     average_marks = sum_of_all_marks // no_of_subjects
    
#     results_dict[student_name] = average_marks

# print(results_dict)



# Write a Python program to create a dictionary from a string. Note: Track the
# count of the letters from the string. Sample string : 'w3resource' Expected output:
# {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}


# dict1 = {}

# str1 = "w3resource"

# for i in str1:
#     if i in dict1.keys():
#         dict1[i] += 1
#     else:
#         dict1[i] = 1 
# print(dict1)



# Question: Pattern problem
#         *
#       *   *
#     *   *   *
#   *   *   *   *

# solution: here the number of colums or rows are = n
# and the number of spaces in the starting are n-i

# n = int(input("Please enter the no of rows "))
# for i in range(1, n+1):
#     print(" " * (n - i), end="")
#     print("* " * i)




# Question: Pattern problem
#         1
#       2   2
#     3   3   3
#   4   4   4   4
# n = n = int(input("Please enter the no of rows "))

# for i in range(1, n+1):
#     print(" " * (n-i), end="")
#     print((str(i) + " ") * (i))



# Question: Pattern problem
# ******
#  *****
#   ****
#    ***
#     **
#      *
# n = n = int(input("Please enter the no of rows "))

# for i in range (1, n+1):
#     print(" " * (i-1), end="")
#     print("*" * (n-i+1))


# Question: Pattern problem
#  * * * * *
#  * * * *  
#  * * *    
#  * *      
#  * 
# n = n = int(input("Please enter the no of rows "))

# for i in range (1, n+1):
#     print("*" * (n-i+1), end="")
#     print(" " * (i-1))


# Question: Pattern problem
#     1     
#    1 2    
#   1 2 3   
#  1 2 3 4  
# 1 2 3 4 5 
# n = n = int(input("Please enter the no of rows "))

# for i in range(1, n+1):
#     print(" " * (n-i), end="")
#     for j in range(1, i+1):
#         print((str(j) + " "), end="")
#     print()



# Authentication system

# def get_username_password(): # user_pass_dict is an argument 
#     print("Please enter your desired username: ")
#     username = input()
#     print("Enter your password: ")
#     password = input()
# # adding key (username) and value (password) in to the dictionary
#     return username, password


# def show_all_users(username_to_password_dict):
#     print(username_to_password_dict.keys())


# print("Authentication system")


# username_to_password_dict = dict() # making of the dictionary
# while True:
#     print("1. To create account")
#     print("2. To login")
#     print("3. To show all users")
#     print("4. to exit")
#     print()



#     x = int(input())

#     if x == 4:
#         print("Thank you, Come back again in future :)")
#         break
#     elif x == 1:
#         username, password =  get_username_password()
#         if username in username_to_password_dict:
#             print("error: username already taken")
#             continue
#         # calling the func. and passing the dictionary as parameter to it,
#         # so that it will get mapped with (user_pass_dict) in the func.
#         # username_to_password_dict = get_username_password(username_to_password_dict)
#         # print(username_to_password_dict)
#         username_to_password_dict[username] = password
        
#     elif x == 2:
#         username_to_password_dict = get_username_password(username_to_password_dict)
#         if username not in username_to_password_dict:
#             print("error: username does not exist")
#             continue
#         expected_password = username_to_password_dict[username]
#         if password == expected_password:
#             print("Login successful")
#         else:
#             print ("Invalid input")
#     elif x == 3:
#         show_all_users(username_to_password_dict)
#     else:
#         print("Invalid input")





def random_func(a, b):
    add = a + b
    sub = a - b
    mult = a * b

    return add, sub, mult

x, y, z = random_func(10, 5)

print(x, y, z)







