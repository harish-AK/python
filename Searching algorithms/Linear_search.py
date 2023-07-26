arr=[1,34,21,90,45,12]
element_need_to_find=21
length=len(arr)
def search(arr,length,element_need_to_find):
    for i in range(0,length):
        if arr[i]==element_need_to_find:
            print("found at  index number ",i," element is ",arr[i])
        # else:
        #     print("element not in array")
    return -1
search(arr,length,element_need_to_find)