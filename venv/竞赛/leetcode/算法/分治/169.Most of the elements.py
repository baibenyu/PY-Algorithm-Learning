# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/22 12:47'
from typing import List


class Solution:
    # 方法一:因为多数元素实际上就是最多元素,利用python自带的couter字典(哈希表)子类的方法来取出
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        most = Counter(nums)
        return most.most_common(1)[0][0]

    # 方法二:排序--因为多数元素的个数要大于总个数的一半,换句话说有序数组中间的元素总是多数元素,无论多数元素值是最大还是最小
    def majorityElement2(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

    # 方法三:分治--如果一个问题的每个最小子问题的答案是显而易见且统一描述的(非相同),那么可以考虑用分治算法来解决
    def majorityElement3(self, nums: List[int]) -> int:
        def majority_element_rec(l, h) -> int:
            # 当将数组分解到只含有一个元素(左右边界相同时),那个元素即为所谓的多数元素
            if l == h:
                return nums[l]

            # 将数组递归分解为左子数组和右子树组
            mid = (h - l) // 2 + l
            left = majority_element_rec(l, mid)
            right = majority_element_rec(mid + 1, h)

            # 如果左右数组的多数元素相同
            if left == right:
                return left

            # 如果不同,在两个数组合并后的范围内统计各自多数元素的个数,返回多的那个
            left_count = sum(1 for i in range(l, h + 1) if nums[i] == left)
            right_count = sum(1 for i in range(l, h + 1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums) - 1)

    # 方法四:摩尔投票法
    # 每一轮投票过程中，从数组中找出一对不同的元素，将其从数组中删除。 这样不断的删除直到无法再进行投票，如果数组为空，则没有任何元素出现的次数超过该数组长度的一半。
    def majorityElement4(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
