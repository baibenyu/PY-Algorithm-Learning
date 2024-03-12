# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/29 15:19'

import time
from typing import List


class Vector2D:
    # 方法一:双指针--用指针来追踪迭代的位置,而不是重新建立一个数据结构
    def __init__(self, v: List[List[int]]):
        self.vector = v
        self.inner = 0
        self.outer = 0

    def advance_to_next(self):  # 判断当前向量是否已全部遍历,并移动到下一个变量
        while self.outer < len(self.vector) and self.inner == len(self.vector[self.outer]):
            self.outer += 1
            self.inner = 0

    def next(self) -> int:
        self.advance_to_next()
        result = self.vector[self.outer][self.inner]
        self.inner += 1
        return result

    def hasNext(self) -> bool:
        self.advance_to_next()
        return self.outer < len(self.vector)


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
