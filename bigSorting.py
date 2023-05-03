


unsorted = ['6', '31415926535897932384626433832795', '1', '3', '10', '3', '5']

# Write your code here
for i in range(len(unsorted)-1):
    key = unsorted[i+1]
    while i >= 0:
        if int(unsorted[i]) > int(key):
            unsorted[i+1] = unsorted[i]
            i -= 1
        elif int(unsorted[i]) <= int(key):
            break
    unsorted[i+1] = key
print(unsorted)
