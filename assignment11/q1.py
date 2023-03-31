# JTMS-14
# a11 p1.py
# Abdullah Rafique
# arafique@jacobs-university.de

i = 1
while i:
    # user input for file name
    name = input("Enter the file name: ")
    # using try to read the file and print the content
    try:
        f = open(name, 'r')
        for a in f:
            print(a, end="")
        f.close()
        break
    # using exception to print the error
    # asking for the file name if there is some error
    except IOError as err:
        print(err)
    except ValueError as arr:
        print(arr)
    except:
        print("Some other error occured for: ", name)
