# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/25 10:08'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n = int(input())
    ans = [0 for _ in range(10001)]
    nums = list(map(int, input().split()))
    for i in range(len(nums)):
        ans[abs(nums[i] - (i + 1))] += 1
    for i in range(10000, -1, -1):
        if ans[i] > 1:
            print(i, ans[i])

    end = time.perf_counter()
    print(end - start)
