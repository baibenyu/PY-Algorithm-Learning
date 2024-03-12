# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/17 15:34'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    import bisect

    n, p = map(int, input().split())
    nums = list(map(int, input().split()))
    ans = 0
    nums.sort()
    for i in range(len(nums)):
        ans = max(bisect.bisect_right(nums, p * nums[i]) - i, ans)
    print(ans)

    end = time.perf_counter()
    print(end - start)
