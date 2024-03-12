# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/20 10:32'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    import math

    num = int(input())
    nums = [int(x) for x in input().split()]
    nums.sort(reverse = True)

    m = int(math.sqrt(num))
    while num % m != 0:
        m -= 1
    n = num // m
    if m < n:
        m, n = n, m

    ans = [[0 for _ in range(n)] for _ in range(m)]
    up, down, left, right = 0, m - 1, 0, n - 1
    i, j = 0, 0
    while left <= right and up <= down:
        if i == 0:
            cur = left
            while cur <= right:
                ans[up][cur] = nums[j]
                j += 1
                cur += 1
            up += 1
        elif i == 1:
            cur = up
            while cur <= down:
                ans[cur][right] = nums[j]
                j += 1
                cur += 1
            right -= 1
        elif i == 2:
            cur = right
            while cur >= left:
                ans[down][cur] = nums[j]
                j += 1
                cur -= 1
            down -= 1
        else:
            cur = down
            while cur >= up:
                ans[cur][left] = nums[j]
                j += 1
                cur -= 1
            left += 1
        i = (i + 1) % 4

    for x in ans:
        for y in x[:-1]:
            print(y, end = " ")
        print(x[-1])

    end = time.perf_counter()
    print(end - start)
