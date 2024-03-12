# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/14 8:31'

import time


class TwoSum:

    def __init__(self):
        import collections
        self.nums = collections.defaultdict(int)

    def add(self, number: int) -> None:
        self.nums[number] += 1

    def find(self, value: int) -> bool:
        for key, values in self.nums.items():
            if value - key == key:
                if values >= 2:
                    return True
            elif value - key in self.nums:
                return True
        return False


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
