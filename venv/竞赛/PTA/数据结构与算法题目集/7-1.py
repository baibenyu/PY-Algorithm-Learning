# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/6 9:09'

import time

if __name__ == '__main__':
    start = time.perf_counter()
    # 经典DP题
    k = int(input())
    list1 = list(map(int, input().strip().split()))
    flag = False
    for each in list1:
        if each < 0:
            continue
        else:
            flag = True
            break
    if flag:
        dp = [float("-inf") for _ in range(k)]
        dp[0] = list1[0]
        for i in range(1, k):
            dp[i] = max(dp[i - 1] + list1[i], list1[i])
        print(max(dp))
    else:
        print(0)

    end = time.perf_counter()
    print(end - start)
