# JTMS-14
# a8 p2.py
# Abdullah Rafique
# arafique@jacobs-university.de

# taking input
l = float(input())
el = float(input())
size = float(input())
# keeping to 1 decimal place
fm = "{0:>5.1f}{1:>7.1f}{2:>8.4f}{3:>12.7f} \n"
# printing
f = open("Output.txt", "w")
f.write("{0:>5}{1:>7}{2:>8}{3:>12}\n".format("inch", "cm", "m", "km"))
i = l
# converting  and giving new value
while (i <= el):
    cm = i*2.54
    m = cm/100
    km = m/1000
    # prinitng in new file
    f.write(fm.format(i, cm, m, km))
    i += size

f.close()
