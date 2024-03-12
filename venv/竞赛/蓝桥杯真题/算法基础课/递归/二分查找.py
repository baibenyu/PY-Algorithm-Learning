# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/16 12:51'

import time

start = time.clock()


def binarysearch(arr, left, right, target):
    if left > right:
        return -1
    else:
        mid = left + (right - left) >> 1
        if arr[mid] > target:
            return binarysearch(arr, mid + 1, right, target)
        elif arr[mid] < target:
            return binarysearch(arr, left, mid - 1, target)
        else:
            return mid


end = time.clock()
print(end - start)
