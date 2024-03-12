# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/6/2 19:45'

import time


def process(arr, l, r):
    if l == r:
        return
    mid = l + (r - l) >> 1
    process(arr, l, mid)
    process(arr, mid + 1, r)
    merge(arr, l, mid, r)


def merge(arr, l, m, r):  # 采用了外排序的算法
    help = [None for _ in range(r - l + 1)]
    i, p1, p2 = 0, l, m + 1
    while p1 <= m and p2 <= r:
        if arr[p1] <= arr[p2]:
            help[i] = arr[p1]
            p1 += 1
        else:
            help[i] = arr[p2]
            p2 += 1
        i += 1
    while p1 <= m:
        help[i] = arr[p1]
        p1 += 1
        i += 1
    while p2 <= m:
        help[i] = arr[p2]
        p2 += 1
        i += 1
    for j in range(len(help)):
        arr[l + j] = help[j]


if __name__ == '__main__':
    start = time.clock()
    """
    经典应用:
    1.小和问题:求一个数组的小和.
    小和--在一个数组中,一个数的左边比该数小的数累加起来,叫做这个数的小和.
    解:先将问题转换为->数组中的每个数在小和计算中出现了几次->以左边数组的数小于右边的数时,说明小和中多加一个左数
    在merge过程中多加一个变量,当且仅当左边数小于右边时,变量+=(r-p2+1)*arr[p1]


    2.逆序对问题:打印一个数组中所有的逆序对
    逆序--一个数据中,左边的数比右边的数大,则这两个数构成逆序对.
    解:小和问题颠倒一下,解法同样不过换成左边数组的数大于右边的数时,说明逆序对多加一个


    """
    end = time.clock()
    print(end - start)
