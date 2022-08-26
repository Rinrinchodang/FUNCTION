def my_list(a,x):
    i=0
    j=0
    while i<len(a) and j<len(x):
        print(a[i]*x[j],end=",")
        j+=1
        i+=1
my_list([2,5,7,8,3],[1,3,4,5,6])