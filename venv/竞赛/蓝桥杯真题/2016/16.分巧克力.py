# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/15 10:38'

import time

# 方法一:遍历所有巧克力,并把能分割的边长的子巧克力数目统计,找到第一个边长数目小于人数的-1
start = time.clock()
n, k = map(int, input().strip().split())
cuts = [0 for _ in range(100001)]
for i in range(n):
    r, c = map(int, input().strip().split())
    small = min(r, c)
    j = 1
    while j <= small:
        cuts[j] += ((r // j) * (c // j))
        j += 1
for x in range(1, 100001):
    if cuts[x] < k:
        print(x - 1)
        break
end = time.clock()
print(end - start)

# 方法二:二分优化,减少判断
n, k = map(int, input().strip().split())
chocolates = []
for i in range(n):
    chocolates.append(tuple(map(int, input().strip().split())))

left, right = 1, 100000
cut = 1
while left <= right:
    mid = (left + right) // 2
    sum_up = 0
    for j in range(len(chocolates)):
        sum_up += (chocolates[j][0] // mid) * (chocolates[j][1] // mid)
    if sum_up >= k:
        left = mid + 1
        cut = mid
    else:
        right = mid - 1
print(cut)