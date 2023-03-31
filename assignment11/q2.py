# JTMS-14
# a11 p2.py
# Abdullah Rafique
# arafique@jacobs-university.de

a = int(input("1st integer: "))
b = int(input("2nd integer: "))

# zerodivision error
try:
    # if no error, printing the division
    print("Division:", a, "/", b, "=", a/b)
except ZeroDivisionError as arr:
    print("Error: ", arr)

# asking for integer
s = input("Enter a string: ")

# type error

try:
    print(s+a)
except TypeError as err:
    print("Error: ", err)

# taking a input
mode = input("Enter the mode of opening the file:")
# using try and except for value error
try:
    f = open('myfile.txt', mode)
    print(f.read())
    f.close()
except ValueError as prr:
    print("Error: ", prr)
