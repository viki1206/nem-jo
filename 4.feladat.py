def pig_latin(szoveg):
    seged=''
    szoveg2=''
    for ch in szoveg:
        if 'a'<=ch<='z':
            seged+=ch
        elif len(seged) != 0:
            for i in range(1, len(seged)):
                szoveg2 += seged[i]
            szoveg2 += seged[0] + 'ay' + ch
            seged = ''
    print(szoveg2)

pig_latin('az a kecske egy nyul')