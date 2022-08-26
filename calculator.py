def calculator(x,y,operation):
    if operation=="add":
        sum=x+y
        print(sum)
    elif operation=="sub":
        sub=x-y
        print(sub)
    elif operation=="mul":
        mul=x*y
        print(mul)
    elif operation=="div":
        div=x%y
        print(div)
calculator(20,25,"add")
calculator(40,3,"sub")
calculator(10,4,"mul")
calculator(40,4,"div")
    
