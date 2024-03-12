# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/24 11:15'

import time


class Solution:
    # 方法一:利用哈希表检测循环
    def isHappy(self, n: int) -> bool:
        isexit = set()
        while True:
            if n not in isexit:
                temp = 0
                isexit.add(n)
                while n:
                    mod = n % 10
                    n //= 10
                    temp += mod ** 2
                n = temp
            else:
                if n == 1:
                    return True
                else:
                    return False

    # 方法二:检测环总是可以想到快慢指针,此处的快慢是调用了几次函数
    def isHappy2(self, n: int) -> bool:
        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum

        slow_runner = n
        fast_runner = get_next(n)
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = get_next(slow_runner)
            fast_runner = get_next(get_next(fast_runner))
        return fast_runner == 1


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
