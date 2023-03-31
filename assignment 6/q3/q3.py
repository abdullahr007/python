# JTMS-14
# a6 p3.py
# Abdullah Rafique
# arafique@jacobs-university.de

# input
file_name = input("Enter file name:")
# reading file
file1 = open(file_name, "r")

word_count = 0
i = 0
str1 = ""

# display and count number of  words in each line of text file
for line in file1:
    i += 1
    words_in_line = len(line.split())
    str1 = str1 + "Words in Line No: " + \
        str(i) + " are : " + str(words_in_line)+"\n"
    word_count += words_in_line
# printing number and lines
print('\n\n' + str1)


file1.close()
