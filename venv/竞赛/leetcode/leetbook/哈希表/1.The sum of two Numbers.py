# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/22 21:59'
from typing import List


class Solution:
    # 方法一:暴力--尝试所有两个数字的组合,直至成功为止
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length - 1):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # 方法二:建立哈希表--存储已经经过的数字,并判断是否有能加和后为target的数字
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:  # 先判断后添加能保证重复出现的元素不会覆盖之前的第一次出现的索引
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []
