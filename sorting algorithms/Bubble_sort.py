arr=[2,1,45,12]
n=len(arr)  # n=4
for i in range(n):  # i is the index of elements.
    for j in range(0,n-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
for i in range(n):
    print(arr[i])
