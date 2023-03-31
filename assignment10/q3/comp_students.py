# JTMS-14
# a10 p3.py
# Abdullah Rafique
# arafique@jacobs-university.de
# importing file student
from student import *


def main():
    # allocation
    S1 = Student("Betty", 2)
    S2 = Student("Alex", 2)
    S3 = Student("Alex", 3)

    # printing
    print("{0} == {1} --> {2}".format(S1.getName(), S2.getName(), S1 == S2))
    print("{0} != {1} --> {2}".format(S1.getName(), S2.getName(), S1 != S2))
    print("{0} == {1} --> {2}".format(S2.getName(), S3.getName(), S2 == S3))
    print("{0}  > {1} --> {2}".format(S1.getName(), S2.getName(), S1 > S2))
    print("{0} >= {1} --> {2}".format(S2.getName(), S3.getName(), S2 >= S3))
    print("{0}  < {1} --> {2}".format(S1.getName(), S3.getName(), S1 < S3))
    print("{0} <= {1} --> {2}".format(S1.getName(), S2.getName(), S1 <= S2))


main()
