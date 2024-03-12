# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/8/9 8:39'

import time
from typing import List


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    # 方法一:BFS--先将索引与id进行映射方便找到位置
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        import collections
        q = collections.deque([])
        ans = 0
        dict1 = {}
        for j in range(len(employees)):
            if employees[j].id == id:
                q.append(id)
                ans += employees[j].importance
            dict1[employees[j].id] = j
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                for each in employees[dict1[cur]].subordinates:
                    q.append(each)
                    ans += employees[dict1[each]].importance

        return ans

    # 方法二:DFS
    def getImportance2(self, employees: List['Employee'], idx: int) -> int:
        mp = {employee.id: employee for employee in employees}

        def dfs(idx: int) -> int:
            employee = mp[idx]
            total = employee.importance + sum(dfs(subIdx) for subIdx in employee.subordinates)
            return total

        return dfs(idx)


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
