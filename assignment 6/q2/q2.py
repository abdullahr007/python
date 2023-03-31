# JTMS-14
# a6 p2.py
# Abdullah Rafique
# arafique@jacobs-university.de

# openfile
f = open('numbers.txt', 'r')
sum = 0
for line in f:
    # using strip to remove newline
    line = line.strip()
    number = int(line)
    sum += number
    # printing
print("the sum is:", sum)
f.close()
