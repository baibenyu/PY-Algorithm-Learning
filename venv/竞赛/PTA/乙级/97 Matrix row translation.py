# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/27 11:30'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n, k, x = map(int, input().split())
    j = 1
    matrix = []
    for i in range(n):
        nums = list(map(int, input().split()))
        if i % 2 == 0:
            nums[j:] = nums[:n - j]
            nums[:j] = [x] * j
            matrix.append(nums)
            j = (j % k + 1)
        else:
            matrix.append(nums)

    for x in range(n):
        cur = 0
        for y in range(n):
            cur += matrix[y][x]
        if x != n - 1:

            print(cur, end = " ")
        else:
            print(cur)

    end = time.perf_counter()
    print(end - start)
