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

    c=b.split(" ")
    b = ""
    for i in range(len(c)):
        d=c[i].find("ay")-1
        seged=c[i][d]
        c[i]=seged+c[i][:len(c[i])-3]
        b+=c[i]+" "
    b=b.capitalize()[:len(b)-1]
    print(b)

pig_latin("The quick brown fox")