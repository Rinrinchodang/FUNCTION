# list=[55,23,10]
# i=0
# sum=""
# while i<len(list):
#     sum+=str(list[i])
#     i+=1
# print(sum)

def list(x):
    i=0
    sum=""
    while i<len(x):
        sum+=str(x[i])
        i+=1
    return sum
print(list([55,23,10]))