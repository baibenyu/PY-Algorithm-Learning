# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/9 17:27'

import time


class MyCircularQueue:

    def __init__(self, k: int):
        self.res = [None for i in range(k)]
        self.k = k
        self.head = -1
        self.tail = -1

    def isEmpty(self) -> bool:
        if self.head == self.tail == -1:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if (self.tail + 1) % self.k == self.head:
            return True
        else:
            return False

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            if self.isEmpty():
                self.head = 0
            self.tail = (self.tail + 1) % self.k
            self.res[self.tail] = value
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.res[self.head] = None
            self.head = (self.head + 1) % self.k
            if self.res[self.tail] is None:
                self.head = -1
                self.tail = -1
            return True
        else:
            return False

    def Front(self) -> int:
        return self.res[self.head] if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.res[self.tail] if not self.isEmpty() else -1


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
