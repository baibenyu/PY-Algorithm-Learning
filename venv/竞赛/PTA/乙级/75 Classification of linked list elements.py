# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/24 9:27'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    linklist = dict()
    Address, n, k = input().split()
    n, k = int(n), int(k)
    for i in range(n):
        cur, data, nextv = input().split()
        linklist[cur] = (int(data), nextv)
    ans1, ans2, ans3 = [], [], []
    cur = Address
    while cur != "-1":
        if linklist[cur][0] < 0:
            ans1.append([cur, linklist[cur][0], linklist[cur][1]])
        elif 0 <= linklist[cur][0] <= k:
            ans2.append([cur, linklist[cur][0], linklist[cur][1]])
        else:
            ans3.append([cur, linklist[cur][0], linklist[cur][1]])
        cur = linklist[cur][1]
    ans = ans1 + ans2 + ans3
    for j in range(len(ans) - 1):
        print(ans[j][0], ans[j][1], ans[j + 1][0])
    print(ans[-1][0], ans[-1][1], -1)

    end = time.perf_counter()
    print(end - start)
