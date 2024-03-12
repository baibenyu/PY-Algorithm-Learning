# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/6/9 15:12'

import time

if __name__ == '__main__':
    start = time.perf_counter()
    """
    总体可抽象为窗口内的值有特定的要求,通过改变窗口的左右边界使得某些值求解
    1.窗口内的最大值
    解:双端队列+单调递减栈,过期时间晚+值大
    """
    end = time.perf_counter()
    print(end - start)
