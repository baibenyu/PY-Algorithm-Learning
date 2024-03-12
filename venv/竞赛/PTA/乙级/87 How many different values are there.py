# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/26 9:33'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n = int(input())
    ans = set()
    for i in range(1, n + 1):
        ans.add(int(i / 2) + int(i / 3) + int(i / 5))
    print(len(ans))

    end = time.perf_counter()
    print(end - start)
