def my(x,y,z):
    i=x
    a=[]
    while i<=y:
        a.append(i)
        i+=z
    return a   
print(my(2,10,2))