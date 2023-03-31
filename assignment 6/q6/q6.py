# JTMS-14
# a6 p6.py
# Abdullah Rafique
# arafique@jacobs-university.de

# defining function

def histogram(lst):
    for n in lst:
        output = ''
        times = n
        # while loop for histogram
        while (times > 0):
            output += '*'
            times = times - 1
            # printing the output
            print(output)

        # creating empty list
lst = []
n = int(input("Enter the element of the list:"))

# iterating the range
for i in range(0, n):
    element = int(input())
    lst.append(element)
    # calling function
histogram(lst)
