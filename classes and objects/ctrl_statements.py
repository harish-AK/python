li=list(range(10))
print(li)
for n in li:
    if n in(3,4,7,9):
        print(n)
        break
    else:
        continue
else:
    pass


if(li[1]==2):
    print("second item is 2")
elif(li[1]==3):
    print("second is 3")
else:
    print('no')
while li[1]==1:
    print("infinite")
    break