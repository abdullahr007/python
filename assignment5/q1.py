# JTMS-14
# a5 p1.py
# Abdullah Rafique
# arafique@jacobs-university.de

# user input
cups = int(input("value for cup:"))
gallons = int(input("value for gallons:"))

# defining function converting and adding


def to_liter(gallon, cup):
    vol1 = gallon * 3.7854
    vol2 = cup * 0.2366

    return vol1 + vol2


# printing outside function and also calling function
print(to_liter(gallons, cups))
