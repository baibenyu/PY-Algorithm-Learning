# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/6/5 14:42'

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


def createGraph(matrix: [[]]):
    graph = Graph()
    for i in range(len(matrix)):
        begin, to, weight = matrix[i][0], matrix[i][1], matrix[i][2]
        if begin not in graph.nodes:
            graph.nodes[begin] = Node(begin)
        if to not in graph.nodes:
            graph.nodes[to] = Node(to)
        b_node, t_node = graph.nodes.get(begin), graph.nodes.get(to)
        newEdge = Edge(weight, b_node, t_node)
        b_node.nexts.add(t_node)
        b_node.outdegree += 1
        t_node.indegree += 1
        b_node.edges.add(newEdge)
        graph.edges.add(newEdge)
    return graph


if __name__ == '__main__':
    start = time.clock()
    """
    1.BFS
    解:队列+去重集合
    2.DFS
    解:栈+去重集合,这是迭代实现,每次加入新点,要将当前点和新点都加入栈中,并立刻跳出循环,栈中此时即为DFS走过的路径,直至当前结点的所有邻居均被访问过,那么返回(pop)上一层
    3.拓扑排序
    解:循环找入度为0的点,并抹消它的影响
    """
    end = time.clock()
    print(end - start)
