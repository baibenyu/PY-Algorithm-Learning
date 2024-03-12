# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/12 22:14'

import collections
import itertools
import time

start = time.clock()

m, n = map(int, input().strip().split())
sum_up = m + n
level = 0
while sum_up:
    level += 1
    sum_up -= level

count = 0
for i in itertools.product(range(2), repeat = level):
    temp_i = list(i)
    temp = collections.Counter(temp_i)
    temp_m = m - temp[0]
    temp_n = n - temp[1]
    temp_level = level - 1
    while (temp_m > 0 or temp_n > 0) and temp_level > 0:
        temp_j = []
        j = 0
        while j < temp_level:
            cur = temp_i[j] ^ temp_i[j + 1]
            temp_j.append(cur)
            if int(cur) == 0:
                temp_m -= 1
            else:
                temp_n -= 1
            j += 1
        temp_i = temp_j
        temp_level -= 1
    if temp_level == 0 and temp_m == 0 and temp_n == 0:
        count += 1

print(count)

end = time.clock()
print(end - start)
