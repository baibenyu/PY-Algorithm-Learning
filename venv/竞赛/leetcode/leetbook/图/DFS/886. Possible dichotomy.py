# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/6 18:56'
import collections
import time


class Solution(object):
    # 方法一:涂色问题,将相邻结点涂为相反颜色,若重复涂色且颜色不同说明冲突,返回False
    # all函数表示iterable内部所有返回值都为True时才返回True
    def possibleBipartition(self, N, dislikes):
        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        color = {}

        def dfs(node, c=0):
            if node in color:
                return color[node] == c
            color[node] = c
            return all(dfs(nei, c ^ 1) for nei in graph[node])

        return all(dfs(node)
                   for node in range(1, N + 1)
                   if node not in color)


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
