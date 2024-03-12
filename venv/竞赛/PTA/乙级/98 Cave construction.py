# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/27 19:30'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n = int(input())
    top = list(map(int, input().split()))
    down = list(map(int, input().split()))
    lower, highest = min(top), max(down)
    if lower > highest:
        print("Yes", lower - highest)
    else:
        print("No", 1 + abs(lower - highest))

    end = time.perf_counter()
    print(end - start)
