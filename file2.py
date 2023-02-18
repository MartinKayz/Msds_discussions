class Car:
    # Class Attributes - Shared by all objects or instances of the class
    mileage = 0
    brand = "Toyota"
    make = "SUVs"
           
    #Constructor 
    """ def __init__(self):
        pass"""

    # Instance or Object attributes - Specific to a particular object or instance
    def __init__(self, year_of_man, model, color, engine):
        self.year_of_man = year_of_man
        self.model = model
        self.color = color
        self.engine = engine

    def increase_mileage(self, distance = 0):
        # ACCEPT THE distance in float
        #distance = float(input("Enter the distance you have covered so far?"))
        #print(type(distance))
        miles_distance = distance * 0.621371
        print(type(miles_distance))
        #print(self.model + " has travelled " + str(miles_distance))
        print(self.model, " has travelled ", miles_distance)




"""
# Creating objects from the class
honda = Car(2000, "V6", "bLUE", "3000cc")
print("I am the Honda object ", honda.model)
bmw = Car(1998, "v2", "red" , "1500cc")
print("I am the BMW object ", bmw.model)

# Accessing all class attributes

print(honda.mileage)
print(bmw.mileage)


# Accessing all object attributes
# Syntax: obj_name.attribute
print("Honda object was made in ", honda.year_of_man)
print("The BMW object is ", bmw.color, " in color")


# Using methods from the class
#Syntax: obj_name.method_name
bmw.increase_mileage(10)
honda.increase_mileage()

"""


## Inheritance Concepts

class Race(Car):
    make = "Race Car"
    mileage = 10
    brand = "Lambo"
    
    def time_to_race(self):
        print("I am racing...")


class Tractor(Car):
    make = "Tractor for farm"
    mileage = 200
    brand = "Caterpillar"

    def time_to_dig(self):
        print("I am digging ..")



class Passenger(Car):
    pass

class Private(Car):
    pass

# Creating objects from child classes
ferrari = Race(2012, "Avante","Red", "7000cc")

fork_lift = Tractor(1995, "Ferguson", "Yellow", "1000cc")

van =  Passenger(1994,"Drone", "White", "3000cc")

# Printing Parent class attributes from the child

print("I am a child class object called ferrari and this is my mileage ", ferrari.mileage)

print("I am a chld called fork lift and this is my make ", fork_lift.make)



# Printing the Child Class attributes belonging to the child
print("I am a child class object called ferrari and this is my model ", ferrari.model)

print("I am a chld called fork lift and this is my color ", fork_lift.color)    


# Using custom methods for the child class
ferrari.time_to_race()
print(ferrari.make)


fork_lift.time_to_dig()
print(fork_lift.brand)


# Using parent methods on the child class object
ferrari.increase_mileage(12)

fork_lift.increase_mileage()


