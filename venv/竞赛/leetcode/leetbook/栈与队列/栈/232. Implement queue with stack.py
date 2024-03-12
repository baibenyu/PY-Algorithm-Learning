# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/29 21:23'

import time


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 初始化输入栈和输出栈
        self.inStack = []
        self.outStack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        # 有新元素进来，进入输入栈
        self.inStack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # 如果为空
        if self.empty():
            return None

        # 如果输出栈不为空，返回输出栈中的元素
        if self.outStack:
            return self.outStack.pop()
        # 输出栈为空,将输入栈的元素压入输出栈
        else:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
            return self.outStack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        # 使用已有的函数 pop
        res = self.pop()
        # pop 函数弹出了 res，所以要再添加回去
        self.outStack.append(res)

        return res

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        # 两个栈都为空，队列才为空
        if not (self.inStack or self.outStack):
            return True

        return False


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
