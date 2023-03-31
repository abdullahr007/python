# JTMS-14
# a5 p8.py
# Abdullah Rafique
# arafique@jacobs-university.de

from os import sep


data = ("Python is a great programming language")

# printing as list
words = data.split()
print(words)
# upper space
cap = data.upper()
print(cap)
# word position
wrd = 'programming'
# using split
x = data.split()
# counting the positon
res = x.index(wrd)+1
print("The location of word is : ", str(res))
# replacing word
replace = data.replace('g', 'G')
print(replace)
