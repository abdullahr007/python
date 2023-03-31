# JTMS-14
# a4 p5.py
# Abdullah Rafique
# arafique@jacobs-university.de

# defining function
def print_rectangle(n, m, c):
    # using for loop to print n and than m
    for i in range(1, n+1):
        for j in range(1, m+1):
            print(c, end="")
        print()


# input from user
n = int(input())
m = int(input())
c = input()
# calling functions
print_rectangle(n, m, c)
