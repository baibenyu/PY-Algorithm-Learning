# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/21 14:29'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    nums = list(map(int, input().split()))
    n = nums[0]
    nums = nums[1:]
    ans = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                ans += nums[i] * 10 + nums[j]
    print(ans)

    end = time.perf_counter()
    print(end - start)
