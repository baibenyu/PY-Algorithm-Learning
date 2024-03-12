# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/6/3 15:37'

import time


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def heapinsert(self, index):  # 自下而上地维护大根堆
    while self.arr[index] > self.arr[(index - 1) // 2]:  # 如果大于父节点,交换,之所以不限制下标是因为升到最高会导致0跟0比较,必然不满足
        self.swap(index, (index - 1) // 2)
        index = (index - 1) // 2


def heapify(self, index, heapsize):  # 自上而下地维护大根堆
    left = index * 2 + 1  # 当前结点的左孩子
    while left < heapsize:
        largest = left + 1 if left + 1 < heapsize and self.arr[left + 1] > self.arr[left] else left  # 取两孩子中较大的
        largest = largest if self.arr[largest] > self.arr[index] else index  # 比较孩子结点是否大于父节点
        if largest == index:  # 若父节点最大无需排序,否则将较大的孩子与父结点交换
            break
        self.swap(index, largest)
        index = largest
        left = index * 2 + 1  # 继续向下比较


def heapsort(arr):
    for i in range(len(arr)):  # 视为数组中的值依次插入时,调整大根堆
        heapinsert(arr, i)
    # for i in range(len(arr), -1, -1):  # 视为一次性给定整个数组时,调整大根堆
    #     heapify(arr, i, len(arr))

    heapsize = len(arr) - 1
    swap(arr, 0, heapsize)
    while heapsize > 0:
        heapify(arr, 0, heapsize)
        heapsize -= 1
        swap(arr, 0, heapsize)


if __name__ == '__main__':
    start = time.clock()
    """
    经典应用:
    1.排序一个几乎有序的数组
    几乎有序--如果把数组排好序,每个元素移动的距离不超过k,并且k相对于数组长度来说较小
    解:小根堆+滑动窗口
    """
    end = time.clock()
    print(end - start)
