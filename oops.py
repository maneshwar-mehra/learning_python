# class Aeroplane:
#     def __init__(self, no_of_windows):
#         # these are attributes
#         self.wings = 2
#         self.seats = 100
#         self.engine = 2
#         self.color = "white"
#         self.no_of_windows = no_of_windows

#     # these are methods. Methods are functions of a class.
#     # self will always be the first argument of functions under class
#     def take_off(self):
#         print("take off")

#     def land(self, message):  # we can also pass argument here
#         print("land")
#         print("Message -", message)

#     def fly(self):
#         print("fly")


# if __name__ == '__main__':

# #   creating a class object
#     indian_airlines = Aeroplane("50") # "50" is no. of seats
#     # methods
#     indian_airlines.take_off()
#     indian_airlines.land("This is the message")
#     indian_airlines.fly()

#     # attributes
#     print(indian_airlines.wings) 
#     print(indian_airlines.color) 
#     print(indian_airlines.no_of_windows)


# Model a real life School in python code which can contain students batches subjects.
# Use classes for Q2

# class School:
#     def __init__(self):
#         # attributes
#         self.buildings = 2
#         self.classrooms = 50
#         self.no_of_teachers = 50
#         self.no_of_students = 1000
#         self.no_of_subjects = 5
#         self.no_batches = 4



# if __name__ == '__main__':
#     air_force_school = School()
#     print(air_force_school.no_of_subjects)

# 4 Principles of OOPs

# 1. Encapsulation
# 2. Abstraction
# 3. Polymorphism
# 4. Inheritance 



# Encapsulation -> hiding the variables and setting Private/Public access on them 
# class Boy:
#     def __init__(self):
#         # attributes
#         self.age = 20
#         # if we put __ before any attribute variable name,
#         # now it is Private and not accessible outside the class
#         self.__hair_color = "black"
#         self.address = "this is the address"


#     # if we want to to access a Private variable then we have to
#     # make a method for it.
#     # methods
#     def print_hair_color(self): # passing arguments which have used in "attributes" in methods are optional
#         print(self.__hair_color)

#     # we have used __ before method name now this method is private also
#     def __reveal_address(self):
#         print(self.address)

#     # this is how to get the address
#     def get_address(self):
#         return self.__reveal_address()



# if __name__ == '__main__':
#     mane = Boy()
#     print(mane.age)
#     mane.print_hair_color()
#     # print(mane.hair_color)
#     # mane.__reveal_address()
#     mane.get_address()


# Inheritence

class Animal:
    def __init__(self, name, age, no_of_legs):
        # attributes
        self.age = age
        self.name = name
        self.no_of_legs = no_of_legs

    # methods
    def walk(self):
        print(self.name, "is walking")

    def sleep(self):
        print(self.name, "is sleeping")


if __name__ == '__main__':

    animal = Animal("Dog", 20, 4)
    animal.walk()
    animal.sleep()


# syntax for Inheritance
# Make a new class, here it is: Dog
# passed Animal class in it 
# now all the Animal "attributes" and "methods" will be present in class Dog 

class Dog(Animal):
    def __init__(self, name, age, no_of_legs):
        super().__init__(name, age, no_of_legs)

if __name__ == '__main__':
    dog = Animal("Pug", 10, 4)
    dog.walk()
    dog.sleep()