# def add(a,b,c,d,e):
#     sum=a+b+c+d+e
#     print(sum)
# add(1,2,3,4,5)

def add(x):
    i=0
    sum=0
    while i<len(x):
        sum+=x[i]
        i+=1
    print(sum)
add([1,2,3,4,5])


