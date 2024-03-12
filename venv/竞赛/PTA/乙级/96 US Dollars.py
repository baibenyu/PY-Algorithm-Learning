# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/27 10:56'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    import math


    def trytemp(length):
        for a in range(length - 3):
            for b in range(a + 1, length - 2):
                for x in range(b + 1, length - 1):
                    for y in range(x + 1, length):
                        if (temp[a] + temp[b] + temp[x] + temp[y]) % each == 0 and temp[a] != temp[b] != temp[x] != \
                                temp[y]:
                            return True
        return False


    k = int(input())
    nums = list(map(int, input().split()))
    for each in nums:
        temp = []
        for i in range(1, int(math.sqrt(each)) + 1):
            if each % i == 0:
                temp.append(i)
                temp.append(each // i)
        length = len(temp)
        if trytemp(length):
            print("Yes")
        else:
            print("No")

    end = time.perf_counter()
    print(end - start)
