# JTMS-14
# a3 p1.py
# Abdullah Rafique
# arafique@jacobs-university.de

# assigning variables
min = int(input("minutes:"))
# converting to hours
hrs = int(min/60)
# finding mintues
mint = int(min-(hrs*60))
# using if else function for fullfilling requirement
if min >= 0:
    print("hours=", hrs, " and min=", mint)
else:
    print("it is a negative value")
