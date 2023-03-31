# JTMS-14
# a5 p7.py
# Abdullah Rafique
# arafique@jacobs-university.de

# user input
s = input()
x = len(s)
while True:
    a = int(input("a:"))
    # setting range
    if a >= x:
        continue
    else:
        break
while True:
    b = int(input("b:"))
    # setting range
    if b >= x + 1:
        continue
    else:
        break

# printing sliced
print(s[a-1:b+1])
