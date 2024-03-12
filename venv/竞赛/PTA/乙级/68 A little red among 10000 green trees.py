# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/22 15:37'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    a = [int(i) for i in input().split()]
    sum1 = []
    result = []
    for i in range(a[1]):
        b = input().split()
        for j in b:
            sum1.append(int(j.strip(' ')))
    for i in sum1:  # 确保独一无二
        if sum1.count(i) is 1:
            result.append(i)
    i = 0
    try:
        while i < len(result):
            n = sum1.index(result[i])
            x = n // a[0] + 1
            y = n % a[0] + 1
            if x - 1 != 0:
                c = (x - 2) * a[0] + y - 1
                if abs(sum1[c] - result[i]) <= a[2]:
                    del result[i]
                    i -= 1
                    continue
            if y - 1 != 0:
                c = (x - 1) * a[0] + y - 1 - 1
                if abs(sum1[c] - result[i]) <= a[2]:
                    del result[i]
                    i -= 1
                    continue
            if x - 1 != 0 and y - 1 != 0:
                c = (x - 2) * a[0] + y - 1 - 1
                if abs(sum1[c] - result[i]) <= a[2]:
                    del result[i]
                    i -= 1
                    continue
            if x - 1 != 0 and y != a[0]:
                c = (x - 2) * a[0] + y + 1 - 1
                if abs(sum1[c] - result[i]) <= a[2]:
                    del result[i]
                    i -= 1
                    continue
            if x != a[1]:
                c = x * a[0] + y - 1
                if abs(sum1[c] - result[i]) <= a[2]:
                    del result[i]
                    i -= 1
                    continue
            if y != a[0]:
                c = (x - 1) * a[0] + y + 1 - 1
                if abs(sum1[c] - result[i]) <= a[2]:
                    del result[i]
                    i -= 1
                    continue
            if x != a[1] and y - 1 != 0:
                c = x * a[0] + y - 1 - 1
                if abs(sum1[c] - result[i]) <= a[2]:
                    del result[i]
                    i -= 1
                    continue
            if x != a[1] and y != a[0]:
                c = x * a[0] + y + 1 - 1
                if abs(sum1[c] - result[i]) <= a[2]:
                    del result[i]
                    i -= 1
                    continue
            i += 1
        if len(result) > 1:
            print('Not Unique')
        else:
            n = sum1.index(result[0])
            x = n // a[0] + 1
            y = n % a[0] + 1
            print("(%d, %d): %d" % (y, x, result[0]))
    except:
        print('Not Exist')

    end = time.perf_counter()
    print(end - start)
