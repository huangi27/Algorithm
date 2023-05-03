

def insertionSort2(n, arr):
    # Write your code here
    for i in range(n-1):
        temp = arr[i+1]
        while i >= 0:
            if temp < arr[i]:
                arr[i+1] = arr[i]
                i -= 1
            else:
                arr[i+1] = temp
                break
        if i == -1:
            arr[i+1] = temp
        print(*arr)

arr = [1, 4, 3, 5, 6, 2]
insertionSort2(6, arr)