# JTMS-14
# a5 p3.py
# Abdullah Rafique
# arafique@jacobs-university.de
import math
# user input
r = float(input("enter float:"))
# defining function


def volume(radius):
    return ((4/3)*(math.pi)*(radius) ** (3))


# printing outside function
print(volume(r))
