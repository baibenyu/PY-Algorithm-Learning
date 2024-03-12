# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/19 11:16'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n = int(input())
    nums = list(map(int, input().split()))

    maxlist, minlist = [], []
    for i in range(n):
        if not maxlist:
            maxlist.append(nums[i])
            minlist.append(nums[n - i - 1])
        else:
            maxlist.append(max(nums[i], maxlist[-1]))
            minlist.append(min(nums[n - i - 1], minlist[-1]))
    ans = []
    for j in range(n):
        if nums[j] == maxlist[j] and nums[j] == minlist[n - j - 1]:
            ans.append(nums[j])

    if ans:
        print(len(ans))
        for each in ans[:-1]:
            print(each, end = " ")
        print(ans[-1])
    else:
        print(0)
        print()

    end = time.perf_counter()
    print(end - start)
