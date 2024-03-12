# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/15 19:55'

import time

start = time.clock()


def insert(nums: list, k):
    if k == 0:
        return
    insert(nums, k - 1)
    x = nums[k]
    index = k - 1
    while index > -1 and x < nums[index]:
        nums[index+1] = nums[index]
        index -= 1
    nums[index+1] = x


end = time.clock()
print(end - start)
