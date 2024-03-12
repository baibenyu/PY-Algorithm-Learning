# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/26 21:00'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    m = int(input())
    nums = list(map(int, input().split()))
    for i in range(m):
        count = 0
        cur = nums[i]
        while cur > 0:
            cur //= 10
            count += 1
        for j in range(1, 10):
            temp = (nums[i] ** 2) * j
            if temp % (10 ** count) == nums[i]:
                print(j, temp)
                break
        else:
            print("No")

    end = time.perf_counter()
    print(end - start)
