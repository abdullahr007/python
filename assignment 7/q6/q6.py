# JTMS-14
# a7 p6.py
# Abdullah Rafique
# arafique@jacobs-university.de

# defining main
def main():
    # function
    sampleDict = {'Physics': 82, 'Math': 85,
                  'History': 75, 'Management': 70, 'Chemistry': 72}
    # printing
    print("Minimum =", min_value_key(sampleDict))

# defining function


def min_value_key(theDictionary):
   # minimum value
    mini = min(theDictionary.values())
    for k in theDictionary:
        if theDictionary[k] == mini:
            return k


main()
