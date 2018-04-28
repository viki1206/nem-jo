def smallest():
    szam=20
    i=2
    while(i<21):
        if szam%i!=0:
            i=2
            szam+=20
        else:
            i+=1
    print(szam)
smallest()
