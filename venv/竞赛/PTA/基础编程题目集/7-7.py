# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/2 11:18'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    hour, minute = map(int, input().split(":"))
    if hour == 0:
        print(f'{hour}:{minute} AM')
    elif hour == 12:
        print(f'{hour}:{minute} PM')
    elif hour > 12:
        print(f'{hour - 12}:{minute} PM')
    else:
        print(f'{hour}:{minute} AM')

    end = time.perf_counter()
    print(end - start)
