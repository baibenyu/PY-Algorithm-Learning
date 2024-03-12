# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/14 19:56'

import time

# 正确但时间复杂度过高,只能拿一半分数
n = int(input().strip())
origin = list(map(int, input().strip().split()))
start = time.clock()
check = dict()
ans = []
for each in origin:
    check[each] = -1

for i in range(n):
    if check[origin[i]] == -1:
        print(-origin[i], end = " ")
    else:
        print(len(set(origin[check[origin[i]] + 1:i])), end = " ")
    check[origin[i]] = i
end = time.clock()
print(end - start)
