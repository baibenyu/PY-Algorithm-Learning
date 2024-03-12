# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/17 20:08'

import time

start = time.clock()


def pow0(n, k):
    if k == 0:
        return 1
    res = n
    ex = 1
    while ex * 2 <= k:
        res *= res
        ex *= 2
    return res * pow0(n, k - ex)


n, k = map(int, input().strip().split())
print(pow0(n, k))

end = time.clock()
print(end - start)
