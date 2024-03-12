# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/26 12:01'
from typing import List


class Solution:
    # 方法一:单指针,进行种类-1次遍历,第一次将所有0移到指针左边,第二次同理,但仅需遍历0之后的数组即可
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        ptr = 0
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
        for i in range(ptr, n):
            if nums[i] == 1:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1

    # 方法二:双指针,用p0指向0序列的末尾,p1指向1序列的末尾
    # 1.p1的下标必须大于p0下标,否则交换时会导致0序列中穿插了1
    # 2.1序列的起始位置必须随着0序列的后移而后移,否则会导致1被交换到当前正在处理的位置
    def sortColors2(self, nums: List[int]) -> None:
        n = len(nums)
        p0 = p1 = 0
        for i in range(n):
            if nums[i] == 1:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
            elif nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                if p0 < p1:  # 只有p0序列指向排好的1序列时,才需要将被交换出去的1再交换到1序列的末尾,即p1所指位置
                    nums[i], nums[p1] = nums[p1], nums[i]
                p0 += 1
                p1 += 1  # 1序列必须随0序列后移而后移

    # 同双指针,但将0序列放在开头,将2序列放在末尾
    def sortColors3(self, nums: List[int]) -> None:
        n = len(nums)
        p0, p2 = 0, n - 1
        i = 0
        while i <= p2:
            while i <= p2 and nums[i] == 2:  # 必须交换直至换过来的数不是2,因为当前下标只会经过一遍
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            if nums[i] == 0:  # 上方代码消除了2的可能
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
            i += 1
