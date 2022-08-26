def speed(n):
    if n<=70:
        print("70")
    elif n>70:
        i=71
        b=0
        while i<=n:
            if i%5==0:
                b+=1
            i+=1
    if b>12:
        print("license suspended")
    else:
        print(b)
speed(85)
speed(135)
                          