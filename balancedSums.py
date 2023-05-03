

def balancedSums(arr):
    # Write your code here
    index = 0
    l_sum = 0
    r_sum = 0
    while index <= len(arr)-1:
        j = index + 1
        for i in range(index):
            l_sum += arr[i]
        for i in range(j, len(arr)):
            r_sum += arr[i]
        if l_sum == r_sum:
            return 'Yes'
        else:
            l_sum = 0
            r_sum = 0
            index += 1
    return 'No'


arr = [2, 0, 0, 0]

print(balancedSums(arr))
