# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/6/2 16:16'

import time


def insertionsort(arr):  # 实现方式:依次扩展范围,使(0,i)范围内升序排序
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            swap(arr, j, j - 1)
            j -= 1


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
