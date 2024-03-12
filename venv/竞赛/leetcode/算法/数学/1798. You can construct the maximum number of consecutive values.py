# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/8 9:27'

import time
from typing import List


class Solution:
    # 方法一:数学
    # 假设数组中若干个元素可以构造出 [0, x] 范围内的所有整数。如果此时我们再多选择一个元素 y，那么这些元素可以构造出 [0, x]
    # 以及[y,y+x] 范围内的所有整数。 如果我们希望这个多选择的元素 y 使得答案变得更大，那么区间 [0, x] 和[y,y+x] 需要满足什么要求？ 由于我们需要从 0
    # 开始构造出尽可能多的连续整数，而不在区间 [0, x] 中的最小整数是 x+1，因此如果 x+1 在区间 [y,y+x] 中，那么元素 yy 就会使得构造出的连续整数的范围从
    # [0, x] 增加到 [0, y+x]；否则，元素 y 不会对答案产生任何影响。这样一来，我们只需要找出数组中还未被选的元素中最小的那个作为 y 即可。
    # 如果 x+1 >= y，那么就可以更新答案区间，否则剩下更大的元素也不会对答案产生任何影响。 初始时我们没有选择任何元素，对应的区间为 [0, 0]。
    # 随后我们将数组中的元素升序排序，然后依次判断是否能更新答案区间即可。
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        x = 0
        for y in coins:
            if y > x + 1:
                break
            x += y
        return x + 1


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
