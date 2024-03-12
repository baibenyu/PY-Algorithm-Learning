# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/5 20:07'

import time
from typing import List


class Solution:
    # 方法一:BFS+哈希表
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        from collections import defaultdict
        # 建立key=start value=list of ends的字典
        dic_red = defaultdict(list)
        dic_blue = defaultdict(list)
        for u, v in redEdges:
            dic_red[u].append(v)
        for u, v in blueEdges:
            dic_blue[u].append(v)
        # res保存可行路径
        min_dist = defaultdict(lambda: float('inf'))
        # que保存可行路径的起点、颜色、已走长度
        # [pos=当前位置(要走路径的起点),color=要走路径的颜色，steps=已走路径的长度(边数)]
        que = [[0, 1, 0], [0, -1, 0]]
        red, blue = 1, -1
        # visited保存已经遍历过的状态
        visited = {(0, 1), (0, -1)}
        while que:
            pos, color, steps = que.pop(0)
            # 更新pos的最短距离 (这点较特别 一般bfs都是求到某个目标点的最短路径 这里需要更新到所有点的)
            min_dist[pos] = min(min_dist[pos], steps)
            dic = dic_red if color == 1 else dic_blue
            for pos_nex in dic[pos]:
                if (pos_nex, -color) not in visited:
                    que.append([pos_nex, -color, steps + 1])
                    visited.add((pos_nex, -color))
        # 最后总结最短路径
        res = []
        for i in range(n):
            if min_dist[i] != float('inf'):
                res.append(min_dist[i])
            else:
                res.append(-1)
        return res


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
