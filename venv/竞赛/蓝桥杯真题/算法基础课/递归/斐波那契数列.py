# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/15 19:41'

import time

start = time.clock()


def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(5))

end = time.clock()
print(end - start)
