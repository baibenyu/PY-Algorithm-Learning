# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/13 19:46'

import time
from math import sqrt

start = time.clock()


# 暴力+剪枝,遍历每个位置可能的值
def f(n):
    for i in range(int(sqrt(n)) + 1):
        for j in range(i, int(sqrt(n)) + 1):
            if i ** 2 + j ** 2 > n:
                break
            for k in range(j, int(sqrt(n)) + 1):
                temp = n - (i ** 2 + j ** 2 + k ** 2)
                if temp < 0:
                    break
                if sqrt(temp) - int(sqrt(temp)) == 0:
                    return i, j, k, int(sqrt(temp))


n = int(input().strip())
a, b, c, d = f(n)
print(a, b, c, d)

end = time.clock()
print(end - start)
