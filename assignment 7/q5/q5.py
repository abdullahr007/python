# JTMS-14
# a7 p5.py
# Abdullah Rafique
# arafique@jacobs-university.de


def main():
    # input for tuple
    tup = ()
    # while if true
    while (1):
        b = int(input("Enter = "))
        if b < 0:
            break
        tup = tup+(b,)
    print(tup)

    new_tup = ()

    for i in reversed(tup):
        new_tup = new_tup+(i,)

    print(new_tup)

    new_tup2 = ()

    i = len(tup)-1
    while i >= 0:
        new_tup2 = new_tup2+(tup[i],)
        i -= 1

    print(new_tup2)


main()
