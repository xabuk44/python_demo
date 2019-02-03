# from lib import bmi

def bmi(mass, height):
    mass_index = mass / (height * height)
    return (mass_index)
print(bmi(106, 1.68))