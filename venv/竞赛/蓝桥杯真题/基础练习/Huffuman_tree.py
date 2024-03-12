# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/5 20:38'

n = int(input().strip())
list1 = list(map(int, input().strip().split()))
cost = 0
for i in range(n-1):
    min1 = min(list1)
    list1.pop(list1.index(min1))
    min2 = min(list1)
    list1.pop(list1.index(min2))
    cost += (min1+min2)
    list1.append(min1+min2)
print(cost)