def perfect(num):
    i=1
    while i<=num:
        sum=0
        j=1
        while j<i:
            if i%j==0:
                sum+=j
            j+=1
        if sum==i:
            print(i,"perfect number")
        i+=1
perfect(1000)