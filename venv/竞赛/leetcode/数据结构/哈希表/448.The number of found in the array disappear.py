# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/22 16:44'
from typing import List


class Solution:
    # 方法一:将数组转为哈希表,遍历[1,n]是否在哈希表内
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set1 = set(nums)
        n = len(nums)
        list1 = list()
        for i in range(1, n + 1):
            if i not in set1:
                list1.append(i)
        return list1

    # 方法二:自己构建一个哈希函数用来更改出现过的元素,未被更改说明未出现
    def findDisappearedNumbers2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for num in nums:
            x = (num - 1) % n  # 当一个数字出现时,它可能已经被更改过(即数组中有重复元素),所以要对n取余
            nums[x] += n  # 出现时,将数组中对应x=num-1下标的数加上n

        ret = [i + 1 for i, num in enumerate(nums) if num <= n]  # 再次遍历数组,若遍历到的数字小于n说明下标+1的数字没出现过,反哈希回来
        return ret
