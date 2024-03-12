# __proindexect_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/24 15:42'
import time
from typing import List


class Solution:
    def gcd(self, x, y):
        if y == 0:
            return x
        else:
            return self.gcd(y, x % y)


s = Solution()
print(s.gcd(24, 20))
