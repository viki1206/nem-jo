def keret(a):
    b=a.split( )
    maximum=0
    for i in range(0,len(b)):
        if ((b[i]) > maximum):
            maximum = len(b[i])
    for i in range(0, len(b)):
        help = '*'
        help += b[i]
        print(help)



keret('A macska szereti  a tejet')