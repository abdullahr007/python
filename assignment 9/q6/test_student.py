# JTMS-14
# a9 p6.py
# Abdullah Rafique
# arafique@jacobs-university.de

from student import *


def main():
    # assigning
    S1 = Student("John", 3, 20)
# for 3 different
    S1.setScore(1, 100)
    S1.setScore(2, 95)
    S1.setScore(3, 50)

    print("Before changing name and Age:")
    print(S1)
# new
    S1.setName("Jack")
    S1.setAge(30)

    print("After changing name and age:")
    print(S1)


main()
