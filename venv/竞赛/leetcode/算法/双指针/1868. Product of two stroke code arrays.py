# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/9 20:26'

import time
from typing import List


class Solution:
    # 方法一:双指针
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:

        def getValue(p1, p2):
            if encoded1[p1][1] == encoded2[p2][1]:
                length, value = encoded1[p1][1], encoded1[p1][0] * encoded2[p2][0]
                p1 += 1
                p2 += 1
            elif encoded1[p1][1] < encoded2[p2][1]:
                length, value = encoded1[p1][1], encoded1[p1][0] * encoded2[p2][0]
                p1 += 1
                encoded2[p2][1] -= length
            else:
                length, value = encoded2[p2][1], encoded1[p1][0] * encoded2[p2][0]
                p2 += 1
                encoded1[p1][1] -= length
            return p1, p2, [value, length]

        p1, p2, ans = 0, 0, []
        while p1 < len(encoded1):
            p1, p2, cur_ans = getValue(p1, p2)
            if ans and cur_ans[0] == ans[-1][0]:
                ans[-1][1] += cur_ans[1]
            else:
                ans.append(cur_ans)
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
