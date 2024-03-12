# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/13 15:27'

import time
import copy


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


start = time.clock()

n = int(input().strip())
headv = Node(None)
cur = headv
nums = []
for each in map(int, input().strip().split()):
    cur.next = Node(each)
    cur = cur.next
    nums.append(each)
cur.next = headv.next
max_gain = float("-inf")

for j in range(n):
    prev = copy.deepcopy(headv)
    cur = prev.next
    gain = 0
    i = 0
    temp = nums.copy()
    while j:
        prev = cur
        cur = cur.next
        j -= 1
    while temp and i < max(temp):
        if cur.val == i + 1:
            temp.remove(i+1)
            gain += i+1
            i = 0
            prev.next = cur.next
            cur.next = None
            cur = prev.next
        else:
            i += 1
            prev = cur
            cur = cur.next
    max_gain = max(gain, max_gain)
print(max_gain)
end = time.clock()
print(end - start)