# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/26 21:08'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n, m = map(int, input().split())
    ans = [0 for _ in range(n)]
    for i in range(m):
        cur = list(map(int, input().split()))
        for j in range(len(cur)):
            ans[j] += cur[j]
    maxnum = max(ans)
    print(maxnum)
    temp = []
    for x in range(len(ans)):
        if ans[x] == maxnum:
            temp.append(str(x + 1))
    print(" ".join(temp))

    end = time.perf_counter()
    print(end - start)
