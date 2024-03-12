# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/29 21:08'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    import collections

    string = input()
    ans = collections.Counter(string)
    total = ans["S"] + ans["t"] + ans["r"] + ans["i"] + ans["n"] + ans["g"]
    i = 0
    while total > 0:
        cur = "String"[i]
        if ans[cur] > 0:
            print(cur, end = "")
            ans[cur] -= 1
            total -= 1
        i = (i + 1) % 6

    end = time.perf_counter()
    print(end - start)
