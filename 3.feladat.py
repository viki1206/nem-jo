def keret(a):
    b=a.split( )
    maximum=0
    for i in range(0,len(b)):
        if (len(b[i]) > maximum):
            maximum = len(b[i])
    help = ''
    for i in range(0, len(b)):
        help = '*'
        help += b[i]
        print(help)
    for i in range(0, maximum + 2):
        help2 += '*' 



keret('A macska szereti  a tejet')