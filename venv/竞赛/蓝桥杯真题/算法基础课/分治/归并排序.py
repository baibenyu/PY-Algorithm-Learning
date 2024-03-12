# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/20 15:07'

import time

start = time.clock()


def merge(a, b):
    c = []
    h = j = 0

    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        c.extend(b[h:])
    else:
        c.extend(a[j:])

    return c


def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists) // 2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)


if __name__ == '__main__':
    a = [14, 2, 34, 43, 21, 19]
    print(merge_sort(a))

end = time.clock()
print(end - start)
