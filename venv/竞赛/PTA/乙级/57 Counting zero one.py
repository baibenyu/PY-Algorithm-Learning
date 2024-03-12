# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/21 14:42'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    string = input().upper()
    sumup = 0
    for each in string:
        if "A" <= each <= "Z":
            sumup += ord(each) - 64
    if sumup > 0:
        print(bin(sumup)[2:].count("0"), bin(sumup).count("1"))
    else:
        print(0, 0)

    end = time.perf_counter()
    print(end - start)
