# JTMS-14
# a7 p4.py
# Abdullah Rafique
# arafique@jacobs-university.de


def main():
    # list input
    lis1 = []
    i = 0
    # loop for 7 intake
    while i < 7:
        tup = input("Enter tuple values separated by whitespace = ")
        x = tup.split()
        lis1.append(tuple(x))
        i += 1
    # printing tuple
    print("Before removing the empty:")
    print(lis1)

    # created list which contains the element t

    list2 = []

    for tuples in lis1:
        # checking if value is present or not
        if (tuples != ()):
            list2.append(tuples)
  # pritning new
    print("After removing the empty tuples:")
    print(list2)
