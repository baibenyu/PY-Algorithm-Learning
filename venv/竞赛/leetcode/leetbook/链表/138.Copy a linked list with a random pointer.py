# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/1 16:07'

import time


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    # 方法一:利用自带的copy库
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        import copy
        return copy.deepcopy(head)

    # 方法二:哈希表
    def copyRandomList2(self, head):
        if not head:
            return None
        # 创建一个哈希表，key是原节点，value是新节点
        d = dict()
        p = head
        # 将原节点和新节点放入哈希表中
        while p:
            new_node = Node(p.val, None, None)
            d[p] = new_node
            p = p.next
        p = head
        # 遍历原链表，设置新节点的next和random
        while p:
            # p是原节点，d[p]是对应的新节点，p.next是原节点的下一个
            # d[p.next]是原节点下一个对应的新节点
            if p.next:
                d[p].next = d[p.next]
            # p.random是原节点随机指向
            # d[p.random]是原节点随机指向  对应的新节点
            if p.random:
                d[p].random = d[p.random]
            p = p.next
        # 返回头结点，即原节点对应的value(新节点)
        return d[head]

    # 方法三:利用链表的指针存储复制出来的结点在原结点之后,省去利用哈希的计算
    def copyRandomList3(self, head):
        if not head:
            return None
        p = head
        # 第一步，在每个原节点后面创建一个新节点
        # 1->1'->2->2'->3->3'
        while p:
            new_node = Node(p.val, None, None)
            new_node.next = p.next
            p.next = new_node
            p = new_node.next
        p = head
        # 第二步，设置新节点的随机节点
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
        # 第三步，将两个链表分离
        p = head
        dummy = Node(-1, None, None)
        cur = dummy
        while p:
            cur.next = p.next
            cur = cur.next
            p.next = cur.next
            p = p.next
        return dummy.next


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
