# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/23 17:13'
from typing import List


class Solution:
    # 方法一:回溯,排列问题
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backing(index: int):
            if index == real:
                ans.append(temp.copy())  # 此处必须添加的是temp此时的副本,若添加的是temp原地址内容,回溯时导致内容为空
                return
            else:
                length = len(nums)
                for i in range(length):
                    temp.append(nums.pop(i))
                    backing(index + 1)
                    nums.insert(i, temp.pop())

        ans = list()
        temp = list()
        real = len(nums)
        backing(0)
        return ans


s = Solution()
s.permute([1, 2, 3])
