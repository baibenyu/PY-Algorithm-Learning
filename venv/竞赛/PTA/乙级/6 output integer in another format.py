# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/13 19:46'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n = input()

    if len(n) == 3:
        for i in range(len(n)):
            if i == 0:
                print("B" * int(n[i]), end = "")
            elif i == 1:
                print("S" * int(n[i]), end = "")
            else:
                for j in range(1, int(n[i]) + 1):
                    if j == int(n[i]):
                        print(j)
                    else:
                        print(j, end = "")
    elif len(n) == 2:
        for i in range(len(n)):
            if i == 0:
                print("S" * int(n[i]), end = "")
            else:
                for j in range(1, int(n[i]) + 1):
                    if j == int(n[i]):
                        print(j)
                    else:
                        print(j, end = "")
    else:
        for j in range(1, int(n[0]) + 1):
            if j == int(n[0]):
                print(j)
            else:
                print(j, end = "")

    end = time.perf_counter()
    print(end - start)
