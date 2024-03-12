# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/30 10:39'

class MaxHeap:
    def __init__(self, arr=[]):
        self.arr = arr
        self.size = len(arr)

    def swap(self, parent, children):
        self.arr[parent], self.arr[children] = self.arr[children], self.arr[parent]

    def heapinsert(self, index):  # 自下而上地维护大根堆
        while self.arr[index] > self.arr[(index - 1) // 2]:  # 如果大于父节点,交换
            self.swap(index, (index - 1) // 2)
            index = (index - 1) // 2

    def heapify(self, index):  # 自上而下地维护大根堆
        left = index * 2 + 1  # 当前结点的左孩子
        while left < self.size:
            largest = left + 1 if left + 1 < self.size and self.arr[left + 1] > self.arr[left] else left  # 取两孩子中较大的
            largest = largest if self.arr[largest] > self.arr[index] else index  # 比较孩子结点是否大于父节点
            if largest == index:  # 若父节点最大无需排序,否则将较大的孩子与父结点交换
                break
            self.swap(index, largest)
            index = largest
            left = index * 2 + 1  # 继续向下比较


"""
1.最值问题,前k个值问题
"""