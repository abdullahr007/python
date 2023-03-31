# JTMS-14
# a9 p5.py
# Abdullah Rafique
# arafique@jacobs-university.de

from student import *


def main():
    # score for student john
    S1 = Student("John", 3)

    S1.setScore(1, 100)
    S1.setScore(2, 95)
    S1.setScore(3, 50)
 # print before name changed
    print("Before changing name:")
    print(S1)
 # new student
    S1.setName("Jack")

    print("After changing name:")
    print(S1)


main()
