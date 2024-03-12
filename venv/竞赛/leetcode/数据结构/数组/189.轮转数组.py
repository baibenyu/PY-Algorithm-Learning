# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/22 21:10'

import time
from typing import List


class Solution:
    # 方法一:找到轮转后各元素的下标与原下标的关系,拷贝一个临时数组
    def rotate(self, nums: List[int], k: int) -> None:
        temp = nums.copy()
        length = len(nums)
        k = k % length  # k可能会大于数组长度,真正起作用的是超出部分,所以要取余数
        k = length - k
        for i in range(length):
            nums[i] = temp[(i + k) % length]

    # 方法二:对数组进行切片,然后以k为分界线的两个数组重新合并取代原数组
    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[n - k:] + nums[:n - k]  # 必须修改元素空间


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
