# JTMS-14
# a6 p5.py
# Abdullah Rafique
# arafique@jacobs-university.de
def main():
    # input for list
    lst = []
    n = int(input("Enter an integer= "))
    print("Enter{} float values:".format(n))
  # using append to add number
    for i in range(n):
        a = float(input("Enter a floating point:"))
        lst.append(a)

    lst2 = []
    for element in lst:
        lst2.append(element)
    print("original list:")
    print_list(lst)
# calling functions
    add(lst, 1.5)
    print("After addition")
    print_list(lst)

    multiply(lst2, 5)
    print("After mulitplying by 5")

    print_list(lst2)

# add funtion


def add(lst, val):
    count = 0
    for i in lst:
        lst[count] = lst[count]+val
        count += 1

# function of multiply


def multiply(lst, val):
    count = 0
    for i in lst:
        lst[count] = lst[count]*val
        count += 1

# printing list


def print_list(lst):
    for i in lst:
        f = float(i)
        print(f)


main()
