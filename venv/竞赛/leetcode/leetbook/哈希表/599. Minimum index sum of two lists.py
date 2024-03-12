# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/12 9:50'

import time
from typing import List


class Solution:
    # 方法一:模拟
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict1 = {data: i for i, data in enumerate(list1)}
        dict2 = {data: i for i, data in enumerate(list2)}
        ans = []
        minindex = float("inf")
        for each in dict1:
            if dict2.get(each, -1) != -1:
                if dict2.get(each, -1) + dict1.get(each, -1) < minindex:
                    minindex = dict2.get(each, -1) + dict1.get(each, -1)
                    ans = [each]
                elif dict2.get(each, -1) + dict1.get(each, -1) == minindex:
                    ans.append(each)
        return ans


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
