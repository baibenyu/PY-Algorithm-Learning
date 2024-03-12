# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/9 16:18'

import math
# 首先想到的是用数组模拟,但内存超限,后来又想直接异或然后转字符串统计1的个数,时间超限
# 手写发现规律,完全平方数总是灭的,所以统计范围内的不完全平方数即可
n, l, r = map(int, input().strip().split())
count = 0
for i in range(l, r + 1):
    if i != int(math.sqrt(i)) ** 2:
        count += 1

print(count)