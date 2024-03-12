# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/13 20:19'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    santence = input().split()
    santence.reverse()
    for i in range(len(santence)):
        if i == len(santence) - 1:
            print(santence[i])
        else:
            print(santence[i], end = " ")

    end = time.perf_counter()
    print(end - start)
