# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/20 14:42'

import time

start = time.clock()


def partition(nums, left, right):
    mid = (left + right) // 2
    if nums[mid] <= nums[left] <= nums[right]:
        cur = left
    elif nums[left] <= nums[mid] <= nums[right]:
        cur = mid
    else:
        cur = right
    nums[left], nums[cur] = nums[cur], nums[left]
    cur = left
    pivot = nums[cur]
    left = left + 1
    right = right
    while left <= right:
        while left <= right and nums[left] <= pivot:
            left += 1
        while left <= right and nums[right] > pivot:
            right -= 1
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
    nums[cur], nums[right] = nums[right], nums[cur]
    return right


def quicksort(nums, left, right):
    if left < right:
        cur = partition(nums, left, right)
        quicksort(nums, left, cur - 1)
        quicksort(nums, cur + 1, right)
    return nums

print(quicksort([2, 3, 2, 1, 4, 5], 0, 5))
end = time.clock()
print(end - start)
