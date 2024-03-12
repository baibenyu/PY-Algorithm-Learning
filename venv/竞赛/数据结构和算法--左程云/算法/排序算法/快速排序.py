# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/6/2 20:41'

import time
from random import random


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr, l, r):
    less, more = l - 1, r  # 比基准值小的右边界,比基准值大的左边界
    while l < more:  # l 表示当前位置
        if arr[l] < arr[r]:
            less += 1
            swap(arr, l, less)
            l += 1
        elif arr[l] > arr[r]:
            more -= 1
            swap(arr, l, more)
        else:
            l += 1
    swap(arr, more, r)
    return [less + 1, more]


def quicksort(arr, l, r):
    if l < r:
        swap(arr, l + int(random() * (r - l + 1)), r)  # 随机选择一个数放在末尾,作为基准数
        p = partition(arr, l, r)
        quicksort(arr, l, p[0] - 1)  # 小于区域
        quicksort(arr, p[1] + 1, r)  # 大于区域


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
