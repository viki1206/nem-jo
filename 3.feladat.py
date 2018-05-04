def keret(a):
    b=a.split( )
    maximum=0
    for i in range(0,len(b)):
        if (len(b[i]) > maximum):
            maximum = len(b[i])
    help = ''
    for i in range(0, maximum + 2):
        help += '*'
    print(help)
    for i in range(0, len(b)):
        help = '*'
        help += b[i]
        for j in range(len(b[i]), maximum):



keret('A macska szereti  a tejet')