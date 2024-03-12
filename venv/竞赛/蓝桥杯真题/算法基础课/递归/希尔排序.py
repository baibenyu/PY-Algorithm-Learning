# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/16 13:05'

import time

start = time.clock()


# 先确定增量,即间隔几个元素为一组,对分好的各组进行插入排序
def shellsort(arr):  # 插入排序就是增量为1的希尔排序
    length = len(arr)
    interval = length // 2
    while interval:
        for i in range(interval, length):
            target = arr[i]
            j = i - interval
            while j > -1 and arr[j] > target:  # 插入排序,循环向前找到比目标值大的位置
                arr[j + interval] = arr[j]
                j -= interval
            arr[j + interval] = target
        interval //= 2  # 增量每次减半,直至为0
    return arr


print(shellsort([1, 2, 34, 4, 3, 5, 5, ]))
end = time.clock()
print(end - start)
