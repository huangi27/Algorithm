

def countingSort2(arr):
    # Write your code here
    largest_value = max(arr)
    bound = largest_value + 1
    result = [0] * bound
    for i in arr:
        result[i] += 1
    sorted_arr = []
    for i in range(len(result)):
        while result[i] > 0:
            sorted_arr.append(i)
            result[i] -= 1
    return sorted_arr


arr = [1, 1, 3, 2, 1]

print(countingSort2(arr))

