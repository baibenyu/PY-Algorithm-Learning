# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/6/7 8:18'

import time


class Edge:  # 带权值的边
    def __init__(self, weight, begin, to):
        self.weight = weight
        self.begin = begin
        self.to = to


class Node:  # 单个结点
    def __init__(self, value=None):
        self.value = value
        self.indegree, self.outdegree = 0, 0
        self.nexts, self.edges = set(), set()


class NodeRecord:
    def __init__(self, node, distance):
        self.node = node
        self.distance = distance


class NodeHeap:
    def __init__(self, size):
        self.nodes = [Node() for _ in range(size)]
        self.heapIndexMap = dict()
        self.distanceMap = dict()
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def isEntered(self, node):  # 是否进入过堆
        return True if node in self.heapIndexMap else False

    def inHeap(self, node):  # 是否尚未确定最短路径,即尚在堆中
        return self.isEntered(node) and self.heapIndexMap.get(node) != -1

    def swap(self, index1, index2):  # 交换在堆中的位置,也交换相应的索引
        self.heapIndexMap[self.nodes[index1]] = index2
        self.heapIndexMap[self.nodes[index2]] = index1
        self.nodes[index1], self.nodes[index2] = self.nodes[index2], self.nodes[index1]

    def insert(self, index):  # 自下而上地维护大根堆
        while self.distanceMap[self.nodes[index]] > self.distanceMap[self.nodes[(index - 1) // 2]]:  # 如果大于父节点,交换
            self.swap(index, (index - 1) // 2)
            index = (index - 1) // 2

    def heapify(self, index):  # 自上而下地维护大根堆
        left = index * 2 + 1  # 当前结点的左孩子
        while left < self.size:
            largest = left + 1 if left + 1 < self.size and self.nodes[left + 1] > self.nodes[left] else left  # 取两孩子中较大的
            largest = largest if self.nodes[largest] > self.nodes[index] else index  # 比较孩子结点是否大于父节点
            if largest == index:  # 若父节点最大无需排序,否则将较大的孩子与父结点交换
                break
            self.swap(index, largest)
            index = largest
            left = index * 2 + 1  # 继续向下比较

    def addOrUpdateOrIgnore(self, node, distance):
        if self.inHeap(node):
            self.distanceMap[node] = min(self.distanceMap.get(node), distance)
            self.insert(self.heapIndexMap.get(node))
        if not self.isEntered(node):
            self.nodes[self.size] = node
            self.heapIndexMap[node] = self.size
            self.distanceMap[node] = distance
            self.insert(self.size)
            self.size += 1
        else:
            pass

    def pop(self):
        newpop = NodeRecord(self.nodes[0], self.distanceMap.get(self.nodes[0]))
        self.size -= 1
        self.swap(0, self.size)
        self.heapIndexMap[self.nodes[self.size]] = -1
        del self.distanceMap[self.nodes[self.size]]
        self.nodes[self.size] = None
        self.heapify(0)
        return newpop


def dijkstra(head, size):
    nodeHeap = NodeHeap(size)
    nodeHeap.addOrUpdateOrIgnore(head, 0)
    res = dict()
    while nodeHeap:
        record = nodeHeap.pop()
        cur = record.node
        distance = record.distance
        for edge in cur.edges:
            nodeHeap.addOrUpdateOrIgnore(edge.to, edge.weight + distance)
        res[cur] = distance
    return res


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
