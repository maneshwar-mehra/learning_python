class Aeroplane:
    def __init__(self, no_of_windows):
        # these are attributes
        self.wings = 2
        self.seats = 100
        self.engine = 2
        self.color = "white"
        self.no_of_windows = no_of_windows

    # these are methods. Methods are functions of a class.
    # self will always be the first argument of functions under class
    def take_off(self):
        print("take off")

    def land(self):
        print("land")

    def fly(self):
        print("fly")


if __name__ == '__main__':

#   creating a class object
    indian_airlines = Aeroplane("50")
    # methods
    indian_airlines.take_off()
    indian_airlines.land()
    indian_airlines.fly()

    # attributes
    print(indian_airlines.wings) 
    print(indian_airlines.color) 
    print(indian_airlines.no_of_windows)
