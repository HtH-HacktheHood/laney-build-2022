from unicodedata import name


print("Hello World")

name = "Henry" # string
age = 25 # integer
years_at_hth = 2.5 # float
plays_basketball = True # boolean
jersey_number = "13" # string

car_name = ["Ford", "Chevy", "Mitsubishi", "Acura", "Jeep", "Jaguar"]
x = 50
my_first_name = "John"

print(f"{name} is a {type(name)}")
print(f"{age} is a {type(age)}")
print(f"{years_at_hth} is a {type(years_at_hth)}")
print(f"{plays_basketball} is a {type(plays_basketball)}")
print(f"{jersey_number} is a {type(jersey_number)}")
print(f"{car_name[-1]} is a {type(car_name[-1])}")

type_dictionary = {}

for car in car_name:
    type_dictionary[car] = type(car)

print(type_dictionary)