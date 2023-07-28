arr = [2, 1, 45, 12]
size = len(arr)  # size = 4

for i in range(size):
    min_index = i
    for j in range(i + 1, size):
        if arr[j] < arr[min_index]:  # Change arr[i] to arr[j]
            min_index = j  # Change i to j
    arr[i], arr[min_index] = arr[min_index], arr[i]
    print(arr[i])
