

def icecreamParlor(m, arr):
    # Write your code here
    two = float('inf')
    for i in range(len(arr)):
        one = arr[i]
        j = i + 1
        while j <= len(arr)-1:
            if arr[j] == m - one:
                two = arr[j]
                break
            j += 1
        if one + two == m:
            break
        else:
            continue
    if one + two == m:
        return i+1, j+1
    else:
        return -1

m = 2
arr = [1, 2]

print(icecreamParlor(m, arr))
