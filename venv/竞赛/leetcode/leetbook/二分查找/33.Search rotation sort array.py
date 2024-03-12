# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/3 20:52'
from typing import List


class Solution:
    # 方法一:二分查找--找下标之间的关系带入变量而不是改变常数!!!
    # 整体思路就是把旋转后的数组转回来,使数组有序,再用二分查找
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if target not in nums:  # 特殊情况
            return -1
        elif length == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        else:  # 一般情况
            cur = 0
            flag = False  # 用于判断旋转后的数组是否有序,False表示有序
            while cur < length - 1:  # 找到旋转点的下标
                if nums[cur] > nums[cur + 1]:
                    flag = True
                    cur += 1
                    break
                cur += 1
            if target in nums[:cur]:  # 这里标明target在旋转点之前还是之后,便于之后分类还原下标
                where = "former"
            else:
                where = "later"
            if flag:  # 若无序,将数组旋转回来变得有序
                nums = nums[cur:] + nums[:cur]

            left, right = 0, length - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    if flag:  # 因为二分查找找到的是数组有序状态下target的下标,但题目要求是在旋转后的状态下,所以要进行下标的还原
                        if where == "former":
                            return mid + cur - length  # 此处建议手写执行 例子[3,5,1],3.才能明白为什么这么还原
                        else:
                            return mid + cur  # 此处建议手写执行 例子[3,5,1],1
                    else:  # 若有序则直接二分查找即可.找到的下标即为target的下标
                        return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

    # 方法二:二分查找
    # 该有序数组分成两分,一定有一部分有序,而另一部分无序,选取开头或者结尾的元素与mid元素的大小关系来确定有序和无序的分布
    # 需多加几个判断条件,有序按正常二分查找即可,无序则继续缩小范围直至二分范围内均有序
    def search2(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
