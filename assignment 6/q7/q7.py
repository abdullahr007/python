# JTMS-14
# a6 p7.py
# Abdullah Rafique
# arafique@jacobs-university.de


lst = []

#n = int(input("Enter:"))
# input for elements
while True:
    # for i in range(0, n):
    element = int(input())
#0 is not input
    if element == 0:
        break
    if element >= 0:
        lst.append(element)
    else:
        print("input not correct.")
        # printing list
print(lst)
# prinitng max and minimum value of list
print("Maximum value:", max(lst))
print("Minimum value:", min(lst))
