# JTMS-14
# a4 p2.py
# Abdullah Rafique
# arafique@jacobs-university.de

# input from user
ch = input("enter a Character:")
n = int(input("enter an integer:"))
# using for and range to print and +1 in range cause it
# prints 1 less value than the given value so it will increase
# n by 1 so it can be printed till required
for a in range(n+1):
    # ascii adding integer and printing it by chaning it to chr
    val = chr(ord(ch) + (a))
    print(val)
