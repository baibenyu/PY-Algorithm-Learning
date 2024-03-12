# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/24 10:08'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n, full = [int(x) for x in input().split()]
    for _ in range(n):
        score = [int(x) for x in input().split()]
        tmp = list()
        for i in score[1:]:
            if 0 <= i <= full:
                tmp.append(i)
        tmp.remove(max(tmp))
        tmp.remove(min(tmp))
        print(int((score[0] + sum(tmp) / len(tmp)) / 2 + 0.5))

    end = time.perf_counter()
    print(end - start)
