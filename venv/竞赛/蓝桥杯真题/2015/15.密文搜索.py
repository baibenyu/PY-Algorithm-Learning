# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/12 16:35'

import time
import collections
# 用滑动数组统计各元素出现的次数,判断是否与已有密码串的元素相同,有就加1,
ori = input().strip()
n = int(input().strip())
start = time.clock()
check = []
for i in range(n):
    temp = collections.Counter(input().strip())
    check.append(temp)
count = 0
for j in range(len(ori) - 7):
    if collections.Counter(ori[j:j + 8]) in check:
        count += 1

print(count)

end = time.clock()
print(end - start)
