# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/20 16:04'

import time

start = time.clock()
nums = list(map(int, input().strip().split()))
left = 0
right = len(nums) - 1
while left <= right:
    while left <= right and nums[left] % 2 != 0:
        left += 1
    while left <= right and nums[right] % 2 != 1:
        right -= 1
    if left < right:
        nums[left], nums[right] = nums[right], nums[left]
print(nums)
end = time.clock()
print(end - start)
