def reverse_list(*x):
    b=[]
    i=-1
    while i>=(-len(x)):
        b.append(x[i])
        # x.reverse()
        i-=1
    print(b)
reverse_list("Z","A","A","B","E","M","A","R","D")