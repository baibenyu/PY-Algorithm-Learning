# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/6 10:49'

import time
from typing import List


class Solution:
    # 方法一:BFS
    def canReach(self, arr: List[int], start: int) -> bool:
        import collections
        if 0 not in arr:
            return False
        if arr[start] == 0:
            return True
        n = len(arr)
        q = collections.deque([start])
        isvis = {start}

        while q:
            temp = q.popleft()
            for each in [temp + arr[temp], temp - arr[temp]]:
                if 0 <= each < n and each not in isvis:
                    if arr[each] == 0:
                        return True
                    isvis.add(each)
                    q.append(each)
        return False


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
