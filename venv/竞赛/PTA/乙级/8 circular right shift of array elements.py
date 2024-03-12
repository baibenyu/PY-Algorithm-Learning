# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/13 20:16'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n, m = map(int, input().split())
    m = m % n
    nums = list(map(int, input().split()))
    nums = nums[n - m:] + nums[:n - m]
    for i in range(len(nums)):
        if i == len(nums) - 1:
            print(nums[i])
        else:
            print(nums[i], end = " ")

    end = time.perf_counter()
    print(end - start)
