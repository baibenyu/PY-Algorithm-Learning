# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/18 15:43'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    import collections

    n = int(input())
    grades = collections.Counter(map(int, input().split()))
    query = list(map(int, input().split()))
    for each in query[1:-1]:
        print(grades[each], end = " ")
    print(grades[query[-1]])

    end = time.perf_counter()
    print(end - start)
