def pig_latin(a):
    seged=''
    b=''
    for ch in a:
        if 'A' <= ch <= 'z':
            seged+=ch
        elif len(seged)!= 0:
            for i in range(1,len(seged)):
                b+=seged[i]
            b+=seged[0]+'ay'+ch
            seged=''


    for i in range(1, len(seged)):
        b += seged[i]
    for i in seged:
        b += i
        break
    b += 'ay'
    b=b.capitalize()
    print(b)
    return 0

pig_latin("The quick brown fox")