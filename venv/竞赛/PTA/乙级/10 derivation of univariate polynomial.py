# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/14 8:37'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    nums = list(map(int, input().split()))
    length = len(nums)
    ans = []
    for i in range(0, length, 2):
        if nums[i + 1] != 0:
            ans.append(nums[i] * nums[i + 1])
            ans.append(nums[i + 1] - 1)

    if not ans:
        print(0, 0, end = "")
    else:
        for j in range(0, len(ans), 2):
            if j != len(ans) - 2:
                print(ans[j], ans[j + 1], end = " ")
            else:
                print(ans[j], ans[j + 1], end = "")

    end = time.perf_counter()
    print(end - start)
