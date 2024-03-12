# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/26 9:05'

import time
from typing import List


class Solution:
    # 方法一:排序+双指针
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                left, right = j + 1, len(nums) - 1
                temp = target - nums[i] - nums[j]
                while left < right:
                    cur = nums[left] + nums[right]
                    if cur == temp:
                        if [nums[i], nums[j], nums[left], nums[right]] not in ans:
                            ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                    elif cur < temp:
                        left += 1
                    else:
                        right -= 1
        return ans


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
