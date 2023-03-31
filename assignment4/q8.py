# JTMS-14
# a4 p8.py
# Abdullah Rafique
# arafique@jacobs-university.de

# function to convert miles to km
def convert(miles):
    return 1.609344 * miles


# input from user
x = float(input("type float:"))
# calling function in print
print(convert(x), "km")
