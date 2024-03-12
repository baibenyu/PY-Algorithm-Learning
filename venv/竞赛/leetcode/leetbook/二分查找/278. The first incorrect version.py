# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/21 17:26'

import time

start = time.clock()


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

def isBadVersion(mid):
    pass


class Solution:
    # 方法一:二分查找
    # 对->右移,错->左移
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


end = time.clock()
print(end - start)
