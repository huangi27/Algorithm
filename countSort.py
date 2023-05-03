def countSort(arr):
    # Write your code here
    sorted_list = [[] for i in range(10)]
    for i in range(len(arr)):
        if i in range(len(arr)//2):
            sorted_list[arr[i][0]].append('-')
        else:
            sorted_list[arr[i][0]].append(arr[i][1])
    for i in range(len(sorted_list)):
        l = 0
        while len(sorted_list[i]) != 0 and l < len(sorted_list[i]):
            print(sorted_list[i][l], end=' ')
            l += 1


arr = [[0,'a'],[1,'b'],[0,'c']]
print(arr)
print('----------')
print(countSort(arr))