# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/14 19:46'

import time

start = time.clock()
n = int(input().strip())
count = 0
# 改变1的位置与原数字相与,得到本身说明该二进制位为1
for i in range(32):
    if n & (1 << i) == (1 << i):
        count += 1
print(count)
# Brian Kernighan算法
count = 0
while n:
    count += 1
    n = n & (n - 1)
print(count)
end = time.clock()
print(end - start)
