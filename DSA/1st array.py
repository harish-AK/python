list1 = [2,3,2,4,3,4,5]
#increasing order
list1.sort()
print(list1)

for i in list1:
    z = list1.count(i)
    print(i,z)
    if z==1:
        print("Number that occurs one time only is :",i)

