# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/8/16 7:54'
import heapq
import time
from collections import deque
from typing import List, Generator


class Solution:
    NEIGHBORS = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]

    # 方法一:BFS
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # 枚举 status 通过一次交换操作得到的状态
        def get(status: str) -> Generator[str, None, None]:
            s = list(status)
            x = s.index("0")
            for y in Solution.NEIGHBORS[x]:
                s[x], s[y] = s[y], s[x]
                yield "".join(s)
                s[x], s[y] = s[y], s[x]

        initial = "".join(str(num) for num in sum(board, []))
        if initial == "123450":
            return 0

        q = deque([(initial, 0)])
        seen = {initial}
        while q:
            status, step = q.popleft()
            for next_status in get(status):
                if next_status not in seen:
                    if next_status == "123450":
                        return step + 1
                    q.append((next_status, step + 1))
                    seen.add(next_status)

        return -1

    # 方法二:A*算法--启发式搜索,根据预估代价函数值(曼哈顿距离 or 两点之间的直线距离)与当前代价(走到当前各自花费几步)总和,选取最小代价,进行有方向的搜索
    def slidingPuzzle2(self, board: List[List[int]]) -> int:
        start = board[0] + board[1]
        # n*m puzzle中，m为奇数时,逆序数对奇偶性要和最终奇偶性相同，否则无解
        if sum(1 for i in range(6) for j in range(i + 1, 6) if start[j] and start[i] > start[j]) % 2 == 1:
            return -1

        def h(cur):
            ans = 0
            # 跳过「空格」，计算其余数值的曼哈顿距离
            for i, x in enumerate(cur):
                if x == 0:
                    continue
                r, c = i // 3, i % 3
                tr, tc = (x - 1) // 3, (x - 1) % 3
                ans += abs(r - tr) + abs(c - tc)
            return ans

        target = [1, 2, 3, 4, 5, 0]
        neis = {0: (1, 3), 1: (0, 2, 4), 2: (1, 5), 3: (0, 4), 4: (1, 3, 5), 5: (2, 4)}
        pq = [(0 + h(start), 0, start)]
        costs = {tuple(start): 0}
        best = set()
        while pq:
            _, step, cur = heapq.heappop(pq)
            if cur == target:
                return step
            best.add(tuple(cur))
            zero = cur.index(0)
            for neiPos in neis[zero]:
                nei = cur[:]
                nei[neiPos], nei[zero] = nei[zero], nei[neiPos]
                if (neiState := tuple(nei)) not in best:
                    if neiState not in costs or step + 1 < costs[neiState]:
                        costs[neiState] = step + 1
                        priority = step + 1 + h(nei)
                        heapq.heappush(pq, (priority, step + 1, nei))


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
