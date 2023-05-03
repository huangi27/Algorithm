

def insertion_sort(n, l):
    for i in range(1, n):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key
    return l

m = 6
arr = [7, 4, 3, 5, 6, 2]
# 4 7 (3) 5 6 2
# 3 4 7 (5) 6 2
# 3 4 5 7 (6) 2
# ...
insertion_sort(m, arr)
print(" ".join(map(str,arr)))