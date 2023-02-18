class Student:
    # Defining class attributes
    name = "Moses"
    access_number = "B24123"
    tuition = 230000
    num_of_sem = 6
    
    #Define Instance / Object Attributes
    """def __init__(self):
        pass
    """

    def __init__(self, age, course):
        self.age = age
        self.course = course

    # Protected and private variable ( _ & __ )

    def pay_tuition(self):
        print("I am paying tuition")


    def total_tuition(self, tuition):
        total = tuition * self.num_of_sem
        print("I am going to pay  " + str(total) + "  tuition this semester")




# Creating objects from the class
emma  = Student(12, "BBA")
denis  = Student(14, "PhD")
martin = Student(10, "Nursery")


"""
# Accessing Instance/Objects Attributes
print(emma._age)
print(denis.course)
print(emma.access_number)
print(martin.course)
print(denis.access_number)
"""

# Using object methods
emma.pay_tuition()
denis.total_tuition(20000)



"""
#Accessing class attributes 
print(my_student.name)
print(ds_student.tuition)
print(ds_student.name)

"""
