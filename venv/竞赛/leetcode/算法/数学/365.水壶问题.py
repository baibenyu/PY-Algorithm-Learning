# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/6 17:36'
import math
import time


class Solution:
    # 方法一:裴蜀定理
    # 对任意两个整数a、b设d是它们的最大公约数。那么关于未知数x和y的线性丢番图方程（称为裴蜀等式）：
    # ax + by = m
    # 有整数解（x,y）当且仅当m是d的倍数。裴蜀等式有解时必然有无穷多个解。
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False
        if x == 0 or y == 0:
            return z == 0 or x + y == z
        return z % math.gcd(x, y) == 0


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
