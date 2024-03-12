# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/13 10:34'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    n = input()
    unit = ['ling', 'yi', 'er', 'san', 'si', 'wu', 'liu', 'qi', 'ba', 'jiu']
    numbers = str(sum(map(int, n)))
    len1 = len(numbers)
    # 采用倒除时会因为整十个位上的零无法被识别
    for i in range(len1):
        number = unit[int(numbers[i])]
        if i == len1 - 1:
            print(number, end = '')
        else:
            print(number, end = ' ')

    end = time.perf_counter()
    print(end - start)
