def list(*letters):
    # list=("I am Navgurukul Student in Bangalore")
    i=0
    a=[]
    # c=0
    # c1=0
    while i<len(letters):
        j=0
        c=0
        c1=0
        while j<len(letters[i]):
            if letters[i][j].isupper():
                # print(c,"capital")
                c+=1
            elif letters[i][j].islower():
                # print(c1,"small")
                c1+=1
            else:
                a.append(letters[i])
            j+=1
        print(c,"capital")
        print(c1,"small")
        i+=1
list("I am Navgurukul Student In Bangalore")