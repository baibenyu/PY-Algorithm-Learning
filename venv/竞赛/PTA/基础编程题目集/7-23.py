# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/4 8:51'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    num = input()
    len1 = len(num)
    if num == '0':
        print('a')
        exit(0)

    k = 0
    for i in num[::-1]:  # 统计末尾的0的个数
        if i != '0':
            break
        k += 1

    k = len1 - k
    for i in range(k):  # 只对处于中间的0处理
        if num[i] != '0':  # 先从数字变到字母,再从处于的位置确定单位
            print(chr(ord('a') + int(num[i])), end = '')
            if len1 - i - 1 == 1 or len1 - i - 1 == 5:
                print('S', end = '')
                if len1 - i - 1 == 5 and num[i + 1] == '0' and i + 1 < len1:
                    print('W', end = '')
            elif len1 - i - 1 == 2 or len1 - i - 1 == 6:
                print('B', end = '')
                if len1 - i - 1 == 6 and num[i + 1] == '0' and i + 1 < len1:
                    print('W', end = '')
            elif len1 - i - 1 == 3 or len1 - i - 1 == 7:
                print('Q', end = '')
                if len1 - i - 1 == 7 and num[i + 1] == '0' and i + 1 < len1:
                    print('W', end = '')
            elif len1 - i - 1 == 4:
                print('W', end = '')
            elif len1 - i - 1 == 8:
                print('Y', end = '')
        else:
            if num[i - 1] != '0':
                print('a', end = '')

    end = time.perf_counter()
    print(end - start)
