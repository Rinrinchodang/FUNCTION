def my(list):
    i=1
    j=1
    sum=0
    sum1=0
    while j<len(list):
        sum+=list[i]
        sum1+=list[j]
        i+=2
        j+=2
    print("sum=",sum)
    print("sum1=",sum1)
my([5,4,0,1,9])