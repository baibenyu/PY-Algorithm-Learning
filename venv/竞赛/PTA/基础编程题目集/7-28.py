# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/4 10:24'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n = int(input())
    list1 = [i for i in range(1, n + 1)]
    j = 0
    cur = 1
    while j < n - 1:
        for i in range(n):
            if list1[i] != 0:  # 某个位置被排除了,那么就不能继续计数
                if cur == 3:
                    list1[i] = 0
                    cur = 1
                    j += 1
                else:
                    cur += 1
    for each in list1:
        if each != 0:
            print(each)

    end = time.perf_counter()
    print(end - start)
