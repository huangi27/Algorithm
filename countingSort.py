

def countingSort(arr):
    # Write your code here
    largest_value = max(arr)
    bound = largest_value + 1
    result = [0] * bound
    for i in arr:
        result[i] += 1
    return result


arr = [1, 1, 3, 2, 1]

print(countingSort(arr))

