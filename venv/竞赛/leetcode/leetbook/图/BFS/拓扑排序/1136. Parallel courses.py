# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/31 11:25'

import time
from typing import List


class Solution:
    # 方法一:拓扑排序--经典,入度为0

    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        indeg = [0] * N
        edges = [[] for i in range(N)]
        for a, b in relations:
            indeg[b - 1] += 1
            edges[a - 1].append(b - 1)
        learn = [i for i in range(N) if indeg[i] == 0]
        term = 0
        while learn:
            next_semester = []
            for cur_class in learn:
                for next_class in edges[cur_class]:
                    indeg[next_class] -= 1
                    if indeg[next_class] == 0:
                        next_semester.append(next_class)
            learn = next_semester
            term += 1
        if sum(indeg) > 0:
            return -1
        return term


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
