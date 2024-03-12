# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/13 8:13'

import time


class Logger:

    def __init__(self):
        self.visited = dict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.visited or timestamp >= self.visited[message] + 10:
            self.visited[message] = timestamp
            return True
        else:
            return False


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
