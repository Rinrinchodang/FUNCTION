def my(b):
    if b==1 or b==2:
        return 1
    else:
        return(my(b-1)+my(b-2))
print(my(8))