# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/6/5 16:20'
import heapq
import time


class Edge:  # 带权值的边
    def __init__(self, weight, begin, to):
        self.weight = weight
        self.begin = begin
        self.to = to


class Node:  # 单个结点
    def __init__(self, value):
        self.value = value
        self.indegree, self.outdegree = 0, 0
        self.nexts, self.edges = set(), set()


class Graph:  # 图,数字与结构之间的连接
    def __init__(self):
        self.nodes = dict()  # 由数字得到具体几号结点
        self.edges = set()  # 结点与哪些其它结点的连接


# 注意:要求无向图!!!
def primMST(graph):  # 具体思路:随机从一个点开始,解锁周围的边,每次弹出最小的边,若邻居结点未访问,结果中加入该边,并加入邻居结点的周围边
    q, res, seen = list(), list(), set()
    heapq.heapify(q)
    graph = Graph()
    for node in graph.nodes.values():  # 随机挑选一个点开始,并且涵盖了森林情况,即有多个连通分量(图)
        if node not in seen:
            seen.add(node)
        for edge in node.edges:  # 维护最小边在栈顶
            heapq.heappush(q, edge)
        while q:
            edge = heapq.heappop(q)  # 弹出最小边
            tonode = edge.to
            if tonode not in seen:  # 是否访问过该结点
                seen.add(tonode)
                res.append(edge)
                for nextedge in tonode.edges:
                    heapq.heappush(q, nextedge)


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
