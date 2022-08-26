# list=[1,[],2,[],3]
# i=0
# j=0
# a=[]
# b=[]
# while i<len(list):
#     if type(list[i])==int:
#         a.append(list[i])
#     elif type(list[i])==[]:
#         b.append(list[i])
#     i=i+1
# print(a)

def my(list):
    i=0
    j=0
    a=[]
    b=[]
    while i<len(list):
        if type(list[i])==int:
            a.append(list[i])
        elif type(list[i])==[]:
            b.append(list[i])
        i+=1
    print(a)
my([1,[],2,[],3])
















