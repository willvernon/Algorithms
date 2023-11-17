arr = [1,9,8,4,3,6]
length = len(arr)

for i in range(length):
    for j in range(length -1 -i):
        if(arr[j] > arr[j + 1]):
            tmp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = tmp
            print(arr)
