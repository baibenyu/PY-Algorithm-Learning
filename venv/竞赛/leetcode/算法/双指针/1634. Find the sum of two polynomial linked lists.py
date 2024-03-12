# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/5 17:12'

import time


# Definition for polynomial singly-linked list.
class PolyNode:
    def __init__(self, x=0, y=0, next=None):
        self.coefficient = x
        self.power = y
        self.next = next


class Solution:
    # 方法一:双指针--根据指数调整两个指针的前进
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        p1 = poly1
        p2 = poly2
        dommy = PolyNode(-1, -1)
        cur = dommy
        while p1 or p2:
            coefficient1 = p1.coefficient if p1 else 0
            coefficient2 = p2.coefficient if p2 else 0
            power1 = p1.power if p1 else 0
            power2 = p2.power if p2 else 0
            if power1 > power2:
                power = power1
                coefficient = coefficient1
                p1 = p1.next
            elif power1 < power2:
                power = power2
                coefficient = coefficient2
                p2 = p2.next
            else:
                power = power1
                coefficient = coefficient2 + coefficient1
                if p1:
                    p1 = p1.next
                if p2:
                    p2 = p2.next
            if coefficient:
                cur.next = PolyNode(coefficient, power)
                cur = cur.next
        return dommy.next


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
