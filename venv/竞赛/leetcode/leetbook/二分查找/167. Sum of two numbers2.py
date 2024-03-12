# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/23 11:11'

import time
from typing import List


class Solution:
    # 方法一:二分查找
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            temp = target - numbers[i]
            if temp in numbers:
                l = i + 1
                r = len(numbers) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if numbers[mid] == temp:
                        return [i + 1, mid + 1]
                    elif numbers[mid] < temp:
                        l = mid + 1
                    else:
                        r = mid - 1

    # 方法二:双指针
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
