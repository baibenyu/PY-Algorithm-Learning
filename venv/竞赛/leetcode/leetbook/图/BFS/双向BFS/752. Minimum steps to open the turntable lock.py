# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/6 17:57'

import time
from collections import Generator, deque
from typing import List


class Solution:
    # 方法一:BFS
    # 枚举4个位置向上和向下转导致的八种状态
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0

        dead = set(deadends)
        if "0000" in dead:
            return -1

        def num_prev(x: str) -> str:
            return "9" if x == "0" else str(int(x) - 1)

        def num_succ(x: str) -> str:
            return "0" if x == "9" else str(int(x) + 1)

        # 枚举 status 通过一次旋转得到的数字
        def get(status: str) -> Generator[str, None, None]:
            s = list(status)
            for i in range(4):
                num = s[i]
                s[i] = num_prev(num)
                yield "".join(s)
                s[i] = num_succ(num)
                yield "".join(s)
                s[i] = num

        q = deque([("0000", 0)])
        seen = {"0000"}
        while q:
            status, step = q.popleft()
            for next_status in get(status):
                if next_status not in seen and next_status not in dead:
                    if next_status == target:
                        return step + 1
                    q.append((next_status, step + 1))
                    seen.add(next_status)

        return -1


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
