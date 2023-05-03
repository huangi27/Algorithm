def insertionSort1(n, arr):
    # Write your code here
    temp = arr[n-1]
    while n-2 >= 0:
        if temp < arr[n-2]:
            arr[n-1] = arr[n-2]
            print(*arr)
        else:
            arr[n-1] = temp
            print(*arr)
            break
        n -= 1
    if n-2 == -1:
        arr[n-2+1] = temp
        print(*arr)

arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
insertionSort1(10, arr)