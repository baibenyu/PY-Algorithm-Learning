# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/6/2 15:41'

import time


def bubblesort(arr):  # 实现方式:将大数冒到后面,进行升序排序
    n = len(arr)
    for i in range(n - 1, -1, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)


def swap(arr, i, j):  # 注意:异或双方位于同一块内存中时,数据会被赋值为0,尽量不要使用该方式
    arr[i] = arr[i] ^ arr[j]
    arr[j] = arr[i] ^ arr[j]
    arr[i] = arr[i] ^ arr[j]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
