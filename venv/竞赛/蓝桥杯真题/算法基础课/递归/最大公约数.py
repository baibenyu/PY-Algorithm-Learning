# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/15 19:50'

import time

start = time.clock()


# 辗转相除法
def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)


print(gcd(10, 4))
end = time.clock()
print(end - start)
