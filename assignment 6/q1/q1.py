# JTMS-14
# a6 p1.py
# Abdullah Rafique
# arafique@jacobs-university.de

f1 = open('input.txt', 'r')
char1 = f1.readline(1)
char2 = f1.readline(1)
# printing characters
print(char1)
print(char2)
f1.close()

f2 = open('output.txt', 'w')
# multipyling ASCII
x = ord(char1)
y = ord(char2)
prod = x*y
# printing
print("product:", prod)
# writing in next file
f2.write(str(prod))
f2.close()
