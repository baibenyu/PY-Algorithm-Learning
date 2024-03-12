# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/5 9:40'
from typing import List


class Solution:
    # 方法一:双指针
    # 从倒数第二个元素开始向前找,直至找到从右向左非递增的位置,记录下标i,此时右边的所有元素都是从左到右降序
    # 从倒数第一个元素开始向前找,直至找到第一个大于a[i]的元素,记录下标为j,交换a[i]和a[j],此时j右边仍为降序,并将i的右边按升序排序
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2  # 要交换至少要有两个元素
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        left, right = i + 1, len(nums) - 1
        while left < right:  # 因为原来是降序,所以只要逆转就能得到升序
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
