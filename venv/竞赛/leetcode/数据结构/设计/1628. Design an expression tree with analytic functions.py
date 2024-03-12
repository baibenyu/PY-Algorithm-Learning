# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/25 16:13'

import time
from abc import ABC, abstractmethod

from sqlite3_api.field_types import List


# 方法一:逆波兰表达式+栈
class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass


class MyNode(Node):
    operators = set(['+', '-', '*', '/'])

    def __init__(self, val=None, op=None, left=None, right=None):
        self.val = val
        self.op = op
        self.left = left
        self.right = right

    def evaluate(self) -> int:
        if self.op and self.left and self.right:
            left_operand = self.left.evaluate()
            right_operand = self.right.evaluate()
            if self.op == '+':
                self.val = left_operand + right_operand
            elif self.op == '-':
                self.val = left_operand - right_operand
            elif self.op == '*':
                self.val = left_operand * right_operand
            elif self.op == '/':
                self.val = left_operand / right_operand
        self.op = None
        self.left = self.right = None
        return int(self.val)


class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []
        for i in postfix:
            if i in MyNode.operators:
                right_operand = stack.pop()
                left_operand = stack.pop()
                stack.append(MyNode(op = i, left = left_operand, right = right_operand))
            else:
                stack.append(MyNode(val = int(i)))
        return stack.pop()


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
