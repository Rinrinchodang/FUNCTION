# def list(*x):
#     i=0
#     while i<len(x):
#         print(x(i[i+1]))
#         i+=1
# list([(1,3),(5,7),(4,6),(9,12),(4,10)])

def list():
    num=([(1,3),(5,7),(4,6),(9,12),(4,10)])
    i=0
    a=[]
    while i<len(num):
        j=0
        c=0
        while j<len(num[i]):
            c+=num[i][j]
            j+=1
        a.append(c)
        i+=1
    print(a)
list()