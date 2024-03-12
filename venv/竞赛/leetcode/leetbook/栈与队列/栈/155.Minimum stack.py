# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/15 15:56'
import math


# 实现在常数时间内取出栈中的最小值
class MinStack:
    # 方法一:同步增加一个最小栈记录每一次入栈后的最小值,两个栈元素出栈和入栈都要同时进行
    def __init__(self, x=None):
        if x is None:
            x = []
        self.x = x
        self.min_stack = [math.inf]

    def push(self, val: int) -> None:
        self.x.append(val)
        self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.x.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.x[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

    class MinStack2:
        # 方法二:不使用辅助栈(额外空间)而在栈中存储[当前元素值-当前最小值(即差值)]来实现最小栈
        def __init__(self):
            self.stack = []
            self.min_value = -1

        def push(self, x: int) -> None:
            if not self.stack:  # 如果栈空,初始化
                self.stack.append(0)  # 一个值与它本身差值为零
                self.min_value = x
            else:
                diff = x - self.min_value
                self.stack.append(diff)
                self.min_value = self.min_value if diff > 0 else x  # 如果入栈元素大于最小值,则不变,否则改为入栈元素

        def pop(self) -> None:
            if self.stack:
                diff = self.stack.pop()
                if diff < 0:
                    top = self.min_value
                    self.min_value = top - diff  # 出栈时如果栈顶就是最小元素,要还原入栈之前的最小值
                else:
                    top = self.min_value + diff
                return top

        def top(self) -> int:
            # 如果栈顶元素小于0,说明即为最小值
            return self.min_value if self.stack[-1] < 0 else self.stack[-1] + self.min_value

        def getMin(self) -> int:
            return self.min_value if self.stack else -1
