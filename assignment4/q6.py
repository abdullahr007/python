# JTMS-14
# a4 p6.py
# Abdullah Rafique
# arafique@jacobs-university.de

# def function
def print_frame(n, m, c):
  # using for loop to print row and columms
    for i in range(n):
        for j in range(m):
            # to set condition to print only in given rows and columns
            if (i == 0 or i == n-1 or j == 0 or j == m-1):
                print(c, end="")
            else:
                print(" ", end="")
    # break function
        print()


# user input
n = int(input())
m = int(input())
c = input()
# calling function
print_frame(n, m, c)
