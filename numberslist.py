def number_list(num):
    i=0
    max=0
    while i<len(num):
        if num[i]>max:
            max=num[i]
        i+=1
    print(max)
number_list([1,2,3,4,5,6,7,10,-2])
#     print(max(number_list))
# number_list([1,2,3,4,5,6,7,10,-2])