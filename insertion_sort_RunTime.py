

def runningTime(arr):
    # Write your code here
    shift = 0
    for i in range(1, len(arr)):
        j = i-1
        key = arr[i]
        while (j >= 0) and (arr[j] > key):
           arr[j+1] = arr[j]
           shift += 1
           j -= 1
        arr[j+1] = key
    return shift



arr = [2, 1, 3, 1, 2]
# 4 7 (3) 5 6 2
# 3 4 7 (5) 6 2
# 3 4 5 7 (6) 2
# ...

print(runningTime(arr))
