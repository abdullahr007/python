# JTMS-14
# a6 p4.py
# Abdullah Rafique
# arafique@jacobs-university.de

# input
file_name = input("Enter file name:")
# opening a file and creating new copy file
file1 = open(file_name, "r")
file2 = open('copy.txt', 'w')
# writing into copy.txt
for line in file1:
    file2.write(line)
file1.close()
file2.close()
