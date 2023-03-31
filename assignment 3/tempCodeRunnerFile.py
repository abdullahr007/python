# JTMS-14
# a3 p7.py
# Abdullah Rafique
# arafique@jacobs-university.de


# assigning variable
n = int(input("number:"))
x = 1

# if loop to set condition for minimum input
while n <= 1:
    # to print n minutes and n seconds n times
    # using while loop as asked, "hun araam hay?""
    if(n==1):
        print(x, "minute =", x*60, "seconds")
    elif(n<1):
        print(x, "minute =", x*60, "seconds")
        x += 1
else:
    print("huh no i won't convert")
