# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/12 16:05'

import time
from collections import defaultdict, deque
from typing import List


class Solution:
    # 方法一:建树+层序遍历
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        graph = defaultdict(set)

        for p, pp in zip(pid, ppid):
            graph[pp].add(p)

        ans = []
        d = deque()
        d.append(kill)
        while d:
            cur = d.popleft()
            ans.append(cur)
            d.extend(graph[cur])

        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
