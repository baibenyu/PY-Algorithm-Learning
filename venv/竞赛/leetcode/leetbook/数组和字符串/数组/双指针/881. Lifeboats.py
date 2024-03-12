# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/26 10:23'

import time
from typing import List


class Solution:
    #  方法一:排序+贪心+双指针
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        people.sort()
        light, heavy = 0, len(people) - 1
        while light <= heavy:
            if people[light] + people[heavy] > limit:  # 过重的人单独坐,最轻和最重的坐
                heavy -= 1
            else:
                light += 1
                heavy -= 1
            ans += 1
        return ans


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
