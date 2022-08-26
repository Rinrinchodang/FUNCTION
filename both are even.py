def list(x,y):
    i=0
    while i<len(x):
        j=0
        while j<len(y):
            if x[i]%2==0 and y[j]%2==0:
                print("both are even")
            else:
                print("both are not even")
            j+=1
            i+=1
list([2,6,18,10,3,75],[6,19,24,12,3,87])

# def num(x,y):
#     i=0
#     while i<len(x):
#         if x[i] and y[i]%2==0:
#             print("both are even")
#         else:
#             print("both are not even")
#         i+=1
# num([2,6,18,10,3,75],[6,19,24,12,3,87])