import sys
from district import District


class COVID19Uganda:


    def __init__(self):
        self.districts = []

    def add_district(self, district):
        self.districts.append(district)

    def we_add_district(self):
        # collect data from the user 
        district_name = input("Enter the district name: ")
        confirmed_cases = input("Enter the number of conformed cases: ")
        hospitalizations = input("Enter the number of hospitalized cases: " )
        deaths =  input("Enter the number of deaths: ")

        # use our class District
        district = District(district_name, confirmed_cases, hospitalizations, deaths)
        self.districts.append(district)

    # Return the number of hopitalizations, confirmd cases, deaths per district
    def get_total_data(self, district_name):
        # To be continued


covid = COVID19Uganda()

# Running our program
covid.we_add_district()

