def my(list):
    i=0
    a=[]
    while i<len(list):
        b=(list[i],list[i+1])
        a.append(b)
        i+=2
    print(a)
my([1,3,5,7,4,6,9,12,4,10])