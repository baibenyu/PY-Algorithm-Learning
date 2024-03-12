# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/15 19:26'

import time

start = time.clock()


# 1.找重复
# 2.找变化
# 3.找边界
def sum_up(nums: list, begin: int):
    if begin == len(nums) - 1:
        return nums[begin]
    else:
        return nums[begin] + sum_up(nums, begin + 1)


print(sum_up([1, 3, 2, 45, 1, 23, 23, 2, 3], 0))
end = time.clock()
print(end - start)
