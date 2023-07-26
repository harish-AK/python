# mid=low+(high-low)/2
# if key(element that need to find) is grester than the mid value move right, if key is less then the mid value move left.
arr = [11, 23, 24, 89, 90, 91, 123, 453, 743]
x = 24
l = 0
r = 8

# search by index not by value mid=l+(r-l)//2 means index value is taken, mid=0+(8-0)//2=4
while l <= r:
    mid = l + (r - l) // 2
    if arr[mid] == x:
        print("Element found at index:", mid)
        break
    elif arr[mid] < x:
        l = mid + 1
    else:
        r = mid - 1
else:
    print("Element not found in the array.")


# in for loop
for i in range(len(arr)):
    mid = l + (r - l) // 2
    if arr[mid] == x:
        print("Element found at index:", mid)
        break
    elif arr[mid] < x:
        l = mid + 1
    else:
        r = mid - 1
else:
    print("Element not found in the array.")