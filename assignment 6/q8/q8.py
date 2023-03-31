# JTMS-14
# a6 p8.py
# Abdullah Rafique
# arafique@jacobs-university.de

def overlapping(list1, list2):
    # set function
    for i in list1:
        for j in list2:
            # true if one element same in both list
            if i == j:
                result = True
                return result

# input for first list


list1 = []
n = int(input("Enter the number of elements:"))
for i in range(0, n):
    element1 = int(input())
    if element1 >= 0:
        list1.append(element1)
    else:
        print("input error.")
    if element1 < 0:
        break
list2 = []
n = int(input("Enter the number of elemetns:"))
for i in range(0, n):
    element2 = int(input())
    if element2 >= 0:
        list1.append(element2)
    else:
        print("input error.")
    if element2 < 0:
        break

print(overlapping(list1, list2))
