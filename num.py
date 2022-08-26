def range(min,max,step):
    i=min
    a=[]
    while i<=max:
        a.append(i)
        i+=step
    return a
min=int(input("enter the number:"))
max=int(input("enter the number:"))
step=int(input("enter the number:"))
print(range(min,max,step))