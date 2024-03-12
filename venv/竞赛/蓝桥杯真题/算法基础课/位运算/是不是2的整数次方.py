# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/14 19:55'

import time

start = time.clock()
n = int(input().strip())
# Brian Kernighan算法,2的整数次幂二进制表示下只有一个1
if n & (n-1) == 0:
    print("True")
else:
    print("False")

end = time.clock()
print(end - start)
