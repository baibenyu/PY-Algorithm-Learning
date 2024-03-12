# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/14 9:23'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    nums = list(map(int, input().split()))
    nums = nums[1:]
    a1, a2, a3, a4, a5 = 0, 0, 0, 0, 0
    flag = 1
    k = 0
    count = 0
    for i in range(len(nums)):
        temp = nums[i] % 5
        if temp == 0:
            if nums[i] % 2 == 0:
                a1 += nums[i]
        elif temp == 1:  # 注意在交错相减的时候可能会得到0,所以要判断是初始0还是计算0
            k = 1
            if flag:
                a2 += nums[i]
            else:
                a2 -= nums[i]
            flag = 1 - flag
        elif temp == 2:
            a3 += 1
        elif temp == 3:
            a4 += nums[i]
            count += 1
        else:
            a5 = max(a5, nums[i])
    if count:
        a4 = f"{a4 / count:.1f}"
    print(a1 if a1 else "N", a2 if k else "N", a3 if a3 else "N", a4 if a4 else "N", a5 if a5 else "N")

    end = time.perf_counter()
    print(end - start)
