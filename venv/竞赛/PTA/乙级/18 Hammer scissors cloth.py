# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/15 8:58'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n = int(input())
    a_all, b_all, a_kinds, b_kinds = [0 for _ in range(3)], [0 for _ in range(3)], [[0, "J"], [0, "C"], [0, "B"]], [
        [0, "J"], [0, "C"], [0, "B"]]
    dict1 = {"J": 0, "C": 1, "B": 2}


    def compare(a, b):
        if a == b:
            return 0
        elif a == "C" and b == "J" or a == "J" and b == "B" or a == "B" and b == "C":
            return 1
        else:
            return -1


    for i in range(n):
        a, b = input().split()
        result = compare(a, b)
        if result == 0:
            a_all[1] += 1
            b_all[1] += 1
        elif result == 1:
            a_kinds[dict1.get(a)][0] += 1
            a_all[0] += 1
            b_all[2] += 1
        else:
            b_kinds[dict1.get(b)][0] += 1
            a_all[2] += 1
            b_all[0] += 1

    a_kinds.sort(key = lambda x: x[1])
    a_kinds.sort(key = lambda x: x[0], reverse = True)
    b_kinds.sort(key = lambda x: x[1])
    b_kinds.sort(key = lambda x: x[0], reverse = True)
    print(a_all[0], a_all[1], a_all[2])
    print(b_all[0], b_all[1], b_all[2])
    print(a_kinds[0][1], b_kinds[0][1])

    end = time.perf_counter()
    print(end - start)
