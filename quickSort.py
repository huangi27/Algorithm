

def quickSort(arr):
    # Write your code here
    pivot = arr[0]
    left = []
    right = []
    equal = [pivot]
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        elif arr[i] > pivot:
            right.append(arr[i])
        else:
            equal.append(arr[i])
    return left + equal + right



arr = [4, 5, 3, 7, 2]

print(quickSort(arr))
