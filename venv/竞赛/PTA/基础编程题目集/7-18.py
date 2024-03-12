# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/3 10:58'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    a1, a2, a3, a4 = map(float, input().split())
    left, right = map(float, input().split())
    leftv, rightv = a1 * left ** 3 + a2 * left ** 2 + a3 * left + a4, a1 * right ** 3 + a2 * right ** 2 + a3 * right + a4
    if leftv == 0:
        print(f"{left:.2f}")
    elif rightv == 0:
        print(f"{right:.2f}")
    else:
        flag = False
        # 因为要保留两位小数,所以阈值最多到三位小数即可保证精度
        while left < right - 0.001:
            mid = left + (right - left) / 2
            curv = a1 * mid ** 3 + a2 * mid ** 2 + a3 * mid + a4
            if curv == 0:
                print(f"{mid:.2f}")
                flag = True
                break
            elif curv * leftv < 0:
                right = mid
                rightv = curv
            else:
                left = mid
                leftv = curv
        if not flag:
            print(f"{left:.2f}")

    end = time.perf_counter()
    print(end - start)
