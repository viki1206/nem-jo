def pig_latin(szoveg):
    seged=''
    szoveg2=''
    for ch in szoveg:
        if 'a'<=ch<='z':
            seged+=ch
    print(seged)

pig_latin('az a kecske egy nyul')