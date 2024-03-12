# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/25 15:40'

import time
from sortedcontainers import SortedList  # 第三方库


class Leaderboard:
    # 方法一:哈希表+堆
    def __init__(self):
        self.s = SortedList()  # 可用小根堆替换实现
        self.ren = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.ren:
            oldfen = self.ren[playerId]
            new = oldfen + score
            self.s.remove(oldfen)
            self.s.add(new)
            self.ren[playerId] = new
        else:
            self.ren[playerId] = score
            self.s.add(score)

    def top(self, K: int) -> int:
        return sum(self.s[-K:])

    def reset(self, playerId: int) -> None:
        a = self.ren[playerId]
        self.s.remove(a)
        del self.ren[playerId]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
