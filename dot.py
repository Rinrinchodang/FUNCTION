def name(*x):
    str=""
    i=0
    while i<len(x):
        j=0
        while j<len(x[i]):
            if x[i][j]==x[i][0]:
                a=x[i][0].upper()
                str+=a+"."
            j+=1
        i+=1
    print(str[0:])
name("pooja","neha")
