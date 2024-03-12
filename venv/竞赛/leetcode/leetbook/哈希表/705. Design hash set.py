# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/12 7:48'

import time


class MyHashSet:
    # 方法一:定长拉链法
    def __init__(self):
        self.buckets = 1000
        self.itemsPerBucket = 1001
        self.table = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets

    def pos(self, key):
        return key // self.buckets

    def add(self, key):
        hashkey = self.hash(key)
        if not self.table[hashkey]:
            self.table[hashkey] = [0] * self.itemsPerBucket
        self.table[hashkey][self.pos(key)] = 1

    def remove(self, key):
        hashkey = self.hash(key)
        if self.table[hashkey]:
            self.table[hashkey][self.pos(key)] = 0

    def contains(self, key):
        hashkey = self.hash(key)
        return (self.table[hashkey] != []) and (self.table[hashkey][self.pos(key)] == 1)

    # 方法二:不定长拉链法
    class MyHashSet:

        def __init__(self):
            self.buckets = 1009
            self.table = [[] for _ in range(self.buckets)]

        def hash(self, key):
            return key % self.buckets

        def add(self, key):
            hashkey = self.hash(key)
            if key in self.table[hashkey]:
                return
            self.table[hashkey].append(key)

        def remove(self, key):
            hashkey = self.hash(key)
            if key not in self.table[hashkey]:
                return
            self.table[hashkey].remove(key)

        def contains(self, key):
            hashkey = self.hash(key)
            return key in self.table[hashkey]


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
