def in2cm_table(l, el, size):
    # formating
    fm = "{0:>5.1f}{1:>7.1f}"
    print("{0:>5}{1:>7}".format("inch", "cm"))
    i = l
# to print all values
    while (i <= el):
        conv = i*2.54
        print(fm.format(i, conv))
        i += size
