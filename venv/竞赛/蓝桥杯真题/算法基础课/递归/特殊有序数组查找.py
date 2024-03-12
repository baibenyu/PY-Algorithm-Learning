# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/17 19:37'

import time

start = time.clock()
# 在一个有序且含有空字符串的数组中查找字符
nums = list(map(int, input().strip().split()))
begin, end = 0, len(nums) - 1
while begin <= end:
    mid = (begin + end) // 2
    while nums[mid] == "":  # 跳过空串
        mid += 1
        if mid > end:
            print(-1)
    if nums[mid] > nums[begin]:
        end = mid - 1
    elif nums[mid] < nums[begin]:
        begin = mid + 1
    else:
        print(mid)
        break
end = time.clock()
print(end - start)
