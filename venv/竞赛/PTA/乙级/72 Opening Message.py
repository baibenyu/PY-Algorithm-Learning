# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/23 10:01'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n, m = map(int, input().split())
    things = set(input().split())
    count = [0, 0]
    for i in range(n):
        temp = input().split()
        cur = []
        for each in temp[2:]:
            if each in things:
                cur.append(each)
                count[1] += 1
        if cur:
            count[0] += 1
            print(f"{temp[0]}: " + " ".join(cur))
    print(count[0], count[1])

    end = time.perf_counter()
    print(end - start)
