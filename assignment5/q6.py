# JTMS-14
# a5 p6.py
# Abdullah Rafique
# arafique@jacobs-university.de

from itertools import count

# defining function


def count_vowels(s):
    # setting vowels
    vowel = set("aeiouAEIOU")
   # using iteration
    count = 0
    for alphabet in s:

        if alphabet in vowel:
            count = count + 1
 # printing vowels in function
    print("Vowels:", count)


# user inout
string = input()
# while loop to break if sting empty
while (len(string) == 0):

    break

# calling function
else:
    count_vowels(string)
