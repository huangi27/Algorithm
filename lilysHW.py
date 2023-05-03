

def lilysHomework(arr):
    # Write your code here
    sorted_arr = sorted(arr)
    count = 0
    for i in range(len(sorted_arr)):
        if arr[i] != sorted_arr[i]:
            tmp_id = arr.index(sorted_arr[i])
            arr[tmp_id] = arr[i]
            arr[i] = sorted_arr[i]
            count += 1
            print(arr)
        else:
            continue
    return count


arr = [3,4,2,5,1] # expected output is '2'

print(lilysHomework(arr))




