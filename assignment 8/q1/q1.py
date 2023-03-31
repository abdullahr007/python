# JTMS-14
# a8 p1.py
# Abdullah Rafique
# arafique@jacobs-university.de

# taking input
l = float(input())
el = float(input())
size = float(input())
# keeping to 1 decimal place
m = "{0:>5.1f}{1:>7.1f}"
# printing
print("{0:>5}{1:>7}".format("inch", "cm"))
i = l
# converting to inches and giving new value
while (i <= el):
    conv = i*2.54
    print(m.format(i, conv))
    i += size
