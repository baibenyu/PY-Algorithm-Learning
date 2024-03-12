# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/15 11:04'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    list1 = list(map(int, input().split()))
    list2 = []
    for i in range(10):
        if list1[i] != 0:
            list2.extend([str(i) for _ in range(list1[i])])

    list2[0], list2[list1[0]] = list2[list1[0]], list2[0]
    print("".join(list2))

    end = time.perf_counter()
    print(end - start)
