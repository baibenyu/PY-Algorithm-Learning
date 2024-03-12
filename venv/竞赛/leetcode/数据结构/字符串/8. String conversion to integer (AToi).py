# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/10 17:05'

import time

INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31


class Automaton:
    # 方法一:DFA--确定性有限状态机
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        # 定义各个状态及转化关系
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }

    # 分辨状态条件
    def get_col(self, c):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)  # 直接用sign标志正负,ans始终为正
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1


class Solution:
    def myAtoi(self, str: str) -> int:
        automaton = Automaton()
        for c in str:
            automaton.get(c)
        return automaton.sign * automaton.ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
