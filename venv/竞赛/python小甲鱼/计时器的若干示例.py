# 导入timeit.timeit
from timeit import timeit

# 看执行1000000次x=1的时间：
timeit('x=1')

# 看x=1的执行时间，执行1次(number可以省略，默认值为1000000)：
timeit('x=1', number = 1)

# 看一个列表生成器的执行时间,执行1次：
timeit('[i for i in range(10000)]', number = 1)

# 看一个列表生成器的执行时间,执行10000次：
timeit('[i for i in range(100) if i%2==0]', number = 10000)


def func():
    s = 0
    for i in range(1000):
        s += i
    print(s)


# timeit(函数名_字符串，运行环境_字符串，number=运行次数)
t = timeit('func()', 'from __main__ import func', number = 1000)
print(t)
