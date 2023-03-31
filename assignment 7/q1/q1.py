# JTMS-14
# a7 p1.py
# Abdullah Rafique
# arafique@jacobs-university.de

def longest_world(lst):

    #lst = lst.split()
    longest = []
    longest_length = 0
# checking longest word and its length
    for i in range(len(lst)):
        if len(lst[i]) > longest_length:
            longest = [lst[i]]
            longest_length = len(lst[i])

    return longest, longest_length


# string input to list
string = input("Write the words:")
string1 = string.split()
# calling and prinitng function
print(longest_world(string1))
