# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/29 16:44'
import random
import time
from collections import defaultdict


class RandomizedCollection:

    def __init__(self):
        self.nums = defaultdict(list)  # dict{int:list} 值为对应下标的列表
        self.stack = []  # list(int)

    def insert(self, val: int) -> bool:
        ret = True if val not in self.nums else False
        self.stack.append(val)
        self.nums[val].append(len(self.stack) - 1)
        return ret

    def remove(self, val: int) -> bool:
        if val in self.nums and self.nums[val] != []:
            last = len(self.stack) - 1
            change = self.nums[val][0]
            if last != change:  # 不同时才需要交换值
                self.stack[last], self.stack[change] = self.stack[change], self.stack[last]
                self.nums[self.stack[change]].remove(last)
                self.nums[self.stack[change]].append(change)
            self.stack.pop()
            self.nums[val].remove(change)
            if not self.nums[val]:
                del self.nums[val]  # 列表为空，则删除键
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.stack)


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
