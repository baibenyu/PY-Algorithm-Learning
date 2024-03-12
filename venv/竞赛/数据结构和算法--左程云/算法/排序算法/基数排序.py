# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/6/3 16:25'

import time


def maxbits(arr):  # 找最高有几位
    largest = float("-inf")
    for i in range(len(arr)):
        largest = max(largest, arr[i])
    res = 0
    while largest != 0:
        res += 1
        largest /= 10
    return res


def getdigit(num, d):
    return num % 10 ** d // 10 ** (d - 1)


def radixsort(arr, l, r, digit):
    radix = 10
    bucket = [None for _ in range(r - l + 1)]
    for d in range(1, digit + 1):
        count = [0 for _ in range(radix)]
        for c in range(l, r + 1):  # 统计该进制位下的数有几个等于j的数
            j = getdigit(arr[c], d)
            count[j] += 1
        for c in range(1, radix):  # 该进制位下小于等于下标值的数有几个
            count[c] = count[c] + count[c - 1]
        for c in range(r, l - 1, -1):  # 通过从右向左遍历,可以实现出桶和入桶
            j = getdigit(arr[c], d)
            bucket[count[j] - 1] = arr[i]
            count[j] -= 1
        j = 0
        for i in range(l, r + 1):
            arr[i] = bucket[j]
            j += 1


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
