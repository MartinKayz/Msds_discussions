class District:
    # Class Attributes
    dist_id:int


    def __init__(self, district_name:str, num_conf:int, num_hos:int, num_dths:int):

        self.district_name = district_name #publically-accessed attr - anywhere
        self._num_conf = num_conf #Protected attr - Class & subclasses
        self.__num_hos = num_hos  #Private attr - Only in the class
        self.num_dths = num_dths  


    def get_info(self):
        return f"{self.district_name} has  {self._num_conf} confirmed cases"

    
    def about_dis(self):
        return self.district_name + "has " + str(self._num_conf) + " confirmed cases"
    

    # Getters and Setters
    """ 
    Getters - Help to access values of encapsulated attributes
    Setters - Help to manipultate values of encap.. attributes

    """

    def get_num_hos(self):
        return self.__num_hos

    def set_num_hos(self, value):
        self.__num_hos = value


        
d1 = District("Kampala", 21, 8, 4)
#print(d1.get_info())
#print(d1.about_dis())
#print(d1.district_name)

# Trying to access a protected variable value
#print(d1._num_conf)

# Trying to access a private viriable
#print(d1.__num_hos)
#- Return an attribute error

# Using our getter
print(d1.get_num_hos())

# Using our setter
d1.set_num_hos(10)
print(d1.get_num_hos())





