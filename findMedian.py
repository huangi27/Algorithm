

def findMedian(arr):
    # Write your code here
    for i in range(1, len(arr)):
        j = i-1
        key = arr[i]
        while (j >= 0) and (arr[j] > key):
           arr[j+1] = arr[j]
           j -= 1
        arr[j+1] = key
    print(arr)
    return arr[len(arr)//2]

m = 7
arr = [7, 4, 3, 5, 6, 2, 2]
# 4 7 (3) 5 6 2
# 3 4 7 (5) 6 2
# 3 4 5 7 (6) 2
# ...
print(findMedian(arr))
