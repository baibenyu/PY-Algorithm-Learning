# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/21 9:38'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n, e, d = input().split()
    n = int(n)
    e = float(e)
    d = int(d)
    possibility, empty = 0, 0
    for i in range(n):
        nums = list(map(float, input().split()))
        k = nums[0]
        nums = nums[1:]
        lower = 0
        for each in nums:
            if each < e:
                lower += 1
        if lower > k // 2:
            if k > d:
                empty += 1
            else:
                possibility += 1
    print(f"{possibility / n:.1%}", f"{empty / n:.1%}")

    end = time.perf_counter()
    print(end - start)
