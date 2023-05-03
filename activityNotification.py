

def activityNotifications(expenditure, d):
    # Write your code here
    notifications = 0
    for i in range(len(expenditure)-d):
        if d % 2 == 0:
            tmp = sorted(expenditure[i:i+d-1])
            median = (tmp[(d)//2 - 1]+tmp[d//2])/2
        else:
            tmp = sorted(expenditure[i:i+d-1])
            median = tmp[d//2]
        if expenditure[i+d] >= 2*median:
            notifications += 1
    return notifications


expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
d = 5
'''
expenditure = [1, 2, 3, 4, 4]
d = 4'''
print(activityNotifications(expenditure, d))



