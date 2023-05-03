

def closestNumbers(arr):
    # sorting
    for i in range(1, len(arr)):
        j = i-1
        key = arr[i]
        while (j >= 0) and (arr[j] > key):
           arr[j+1] = arr[j]
           j -= 1
        arr[j+1] = key
    print(arr)
    mini_diff = float('inf')
    arr_ = []
    for i in range(len(arr)-1):
        if abs(arr[i+1] -  arr[i]) < mini_diff:
            mini_diff = abs(arr[i+1] -  arr[i])
            if len(arr_) != 0:
                arr_.clear()
            arr_.append(arr[i])
            arr_.append(arr[i+1])
        elif abs(arr[i+1] -  arr[i]) == mini_diff:
            arr_.append(arr[i])
            arr_.append(arr[i+1])
    return arr_
arr = [-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854]

print(closestNumbers(arr))

