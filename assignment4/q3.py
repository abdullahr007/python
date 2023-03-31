# JTMS-14
# a4 p3.py
# Abdullah Rafique
# arafique@jacobs-university.de


# using while for asking user input for character
while True:
    data = input("enter char: ")
    if not data.isupper():
        continue
    else:
        # we're ready to exit the loop.
        break
# asking for int while loop to ask for user input until valid
while True:
    num = int(input("enter number:"))
    # setting range
    if num <= 0 or num >= 32:
        continue
    else:
        break


for a in range(num+1):
    # ascii adding integer and printing it by chaning it to chr
    val = chr(ord(data) + (a))
    print(val)
