# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/6/2 16:37'

import time
from typing import List


def binarysearch(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


if __name__ == '__main__':
    start = time.clock()
    """
    经典应用:
    1.在一个有序数组中查找某个数
    2.在一个有序数组中查找大(小)于某个数距离最左(右)侧的位置
    3.在无序数组中,任意两个相邻的数不相等,找到一个局部最小(大)值
    局部最小值:超出下标范围视为无穷小或无穷大,arr[i-1]<arr[i]<arr[i+1],arr[i]即为局部最小值
    """
    end = time.clock()
    print(end - start)
