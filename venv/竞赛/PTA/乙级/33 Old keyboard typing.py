# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/17 16:20'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    broken = input()
    isUpper = True
    if "+" in broken:
        isUpper = False

    target = input()
    for each in target:
        if each.upper() not in broken:
            if "A" <= each <= "Z" and not isUpper:
                pass
            else:
                print(each, end = "")

    end = time.perf_counter()
    print(end - start)
