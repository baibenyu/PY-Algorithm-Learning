# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/16 16:56'

import time

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':

        if head == None: # 若链表为空则建立新链表
            newNode = Node(insertVal, None)
            newNode.next = newNode
            return newNode

        prev, curr = head, head.next
        toInsert = False

        while True:

            if prev.val <= insertVal <= curr.val: # 找到插入位置
                # Case #1.
                toInsert = True
            elif prev.val > curr.val:
                # Case #2. where we locate the tail element
                # 'prev' points to the tail, i.e. the largest element!
                if insertVal >= prev.val or insertVal <= curr.val:
                    toInsert = True

            if toInsert:
                prev.next = Node(insertVal, curr)
                # mission accomplished
                return head

            prev, curr = curr, curr.next
            # loop condition
            if prev == head: # 遍历过一次
                break
        # Case #3.
        # did not insert the node in the loop
        prev.next = Node(insertVal, curr)
        return head


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
