# JTMS-14
# a7 p7.py
# Abdullah Rafique
# arafique@jacobs-university.de


def main():
 # dicitonary
    sampleDict = {'Physics': 82, 'Math': 85,
                  'History': 75, 'Management': 70, 'Chemistry': 72}
 # input from user
    key = input("Enter the key value = ")

    a = sampleDict.get(key, None)
 # checking if key is present or not
    if a == None:
        print("The key does not exist!")
    else:
        print("The key has the following value:", a)


main()
