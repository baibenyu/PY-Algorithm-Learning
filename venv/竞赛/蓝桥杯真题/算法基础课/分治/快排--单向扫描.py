import time

start = time.clock()


def partition(nums, left, right):
    pivot = nums[left]
    sp = left + 1  # 扫描指针
    bigger = right  # 大数指针
    while sp <= bigger:
        if nums[sp] <= pivot:  # 遇到小于当前目标值的忽略,下标+1
            sp += 1
        else:  # 否则就与大数指针交换,并让大数指针-1
            nums[sp], nums[bigger] = nums[bigger], nums[sp]
            bigger -= 1
    nums[left], nums[bigger] = nums[bigger], nums[left]  # 将目标值放到正确位置
    return bigger


def quicksort(nums, left, right):
    if left < right:
        cur = partition(nums, left, right)
        quicksort(nums, left, cur - 1)
        quicksort(nums, cur + 1, right)
    return nums


print(quicksort([2, 3, 2, 1, 4, 5], 0, 5))
end = time.clock()
print(end - start)
