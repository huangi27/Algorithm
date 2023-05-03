

def missingNumbers(arr, brr):
    # Write your code here
    largest_value_a = max(arr)
    largest_value_b = max(brr)
    bound_a = largest_value_a + 1
    bound_b = largest_value_b + 1
    result_a = [0] * bound_a
    result_b = [0] * bound_b
    missing_list = []
    for i in arr:
        result_a[i] += 1
    for i in brr:
        result_b[i] += 1

    for i in range(len(result_b)):
        if result_b[i] != 0 and result_b[i] > result_a[i]:
            missing_list.append(i)
    return missing_list
        

'''arr = [7, 2, 5, 3, 5, 3]
brr = [7, 2, 5, 4, 6, 3, 5, 3]'''

arr = [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
brr = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]

print(missingNumbers(arr, brr))

