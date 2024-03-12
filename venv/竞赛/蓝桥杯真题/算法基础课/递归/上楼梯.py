# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/17 19:05'

import time

start = time.clock()


def f(n):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return f(n - 1) + f(n - 2) + f(n - 3)


n = int(input().strip())
print(f(n))
end = time.clock()
print(end - start)
