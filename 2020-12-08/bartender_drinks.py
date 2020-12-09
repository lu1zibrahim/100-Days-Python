def get_drink_by_profession(param):
    my_dict = {
        "Jabroni":"Patron Tequila",
        "School Counselor":"Anything with Alcohol",
        "Programmer":"Hipster Craft Beer",
        "Bike Gang Member":"Moonshine",
        "Politician":"Your tax dollars",
        "Rapper":"Cristal",
    }
    return my_dict.get(param.title(),"Beer")


#This one from Haksell, takes out the list, with all the names in lower case, cleaver
"""
CLICHES = {
    "jabroni": "Patron Tequila",
    "school counselor": "Anything with Alcohol",
    "programmer": "Hipster Craft Beer",
    "bike gang member": "Moonshine",
    "politician": "Your tax dollars",
    "rapper": "Cristal",
}

def get_drink_by_profession(param):
    return CLICHES.get(param.lower(), "Beer")

"""

