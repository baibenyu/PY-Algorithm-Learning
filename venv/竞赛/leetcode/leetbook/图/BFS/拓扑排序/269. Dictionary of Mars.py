# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/31 14:38'

import time
from collections import defaultdict
from itertools import pairwise
from typing import List


class Solution:
    # 方法一:拓扑排序+DFS
    def alienOrder(self, words: List[str]) -> str:
        g = {}
        # 建图
        for c in words[0]:
            g[c] = []
        for s, t in pairwise(words):
            for c in t:
                g.setdefault(c, [])
            for u, v in zip(s, t):
                if u != v:
                    g[u].append(v)
                    break
            else:
                if len(s) > len(t):  # 若前面的字母均相同,但前个单词较短,说明不合法
                    return ""

        VISITING, VISITED = 1, 2
        states = {}
        order = []

        def dfs(u: str) -> bool:
            states[u] = VISITING
            for v in g[u]:
                if v not in states:
                    if not dfs(v):
                        return False
                elif states[v] == VISITING:
                    return False
            order.append(u)
            states[u] = VISITED
            return True

        return ''.join(reversed(order)) if all(dfs(u) for u in g if u not in states) else ""

    # 方法二:拓扑排序+BFS
    def alienOrder2(self, words: List[str]) -> str:
        g = defaultdict(list)
        inDeg = {c: 0 for c in words[0]}
        for s, t in pairwise(words):
            for c in t:
                inDeg.setdefault(c, 0)
            for u, v in zip(s, t):
                if u != v:
                    g[u].append(v)
                    inDeg[v] += 1
                    break
            else:
                if len(s) > len(t):
                    return ""

        q = [u for u, d in inDeg.items() if d == 0]
        for u in q:
            for v in g[u]:
                inDeg[v] -= 1
                if inDeg[v] == 0:
                    q.append(v)
        return ''.join(q) if len(q) == len(inDeg) else ""


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
