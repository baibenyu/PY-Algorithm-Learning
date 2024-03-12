# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/19 9:29'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    import collections

    string = collections.Counter(input())

    total = string["P"] + string["A"] + string["T"] + string["e"] + string["s"] + string["t"]

    while total > 0:
        if string["P"] > 0:
            print("P", end = "")
            string["P"] -= 1
            total -= 1
        if string["A"] > 0:
            print("A", end = "")
            string["A"] -= 1
            total -= 1
        if string["T"] > 0:
            print("T", end = "")
            string["T"] -= 1
            total -= 1
        if string["e"] > 0:
            print("e", end = "")
            string["e"] -= 1
            total -= 1
        if string["s"] > 0:
            print("s", end = "")
            string["s"] -= 1
            total -= 1
        if string["t"] > 0:
            print("t", end = "")
            string["t"] -= 1
            total -= 1

    end = time.perf_counter()
    print(end - start)
