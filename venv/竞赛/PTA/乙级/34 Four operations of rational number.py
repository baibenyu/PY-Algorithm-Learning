# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/18 10:03'

import time


class Fraction:
    # 默认分母=1，且是正数（flag=""正数，flag="-"负数）
    def __init__(self, top, bottom=1):
        is_positive = 1
        if top*bottom < 0:
            is_positive = -1

        # 全都转化成正数
        top, bottom = abs(top), abs(bottom)

        # 分子分母化简
        max_factor = gcd(top, bottom)

        if bottom != 0:
            # 约分
            self.num = is_positive * (top//max_factor)
            self.den = bottom // max_factor
        else:
            # 分母为0，分式没有意义
            self.num = 0
            self.den = 0

    # 显示数据
    def show(self):
        num, den = self.num, self.den

        # 判断是否是正数
        is_positive = 1
        if num*den < 0:
            is_positive = -1

        # 全部转化成正数
        num, den = abs(num), abs(den)

        # 分母为0
        if den == 0:
            return "Inf"

        # 分子为0
        if num == 0:
            return 0

        # 分母为1
        if den == 1:
            if is_positive == 1:
                return "%d" % num
            else:
                return "(-%d)" % num

        # 最简化有理数
        int_num = num // den
        num = num % den

        if int_num == 0:
            # 正负判定
            if is_positive != 1:
                return "(-%d/%d)" % (num, den)
            else:
                return "%d/%d" % (num, den)
        else:
            # 正负判定
            if is_positive != 1:
                return "(-%d %d/%d)" % (int_num, num, den)
            else:
                return "%d %d/%d" % (int_num, num, den)

    # 加法
    def __add__(self, other):
        # 通分
        x = self.num*other.den + self.den*other.num
        y = self.den * other.den

        return Fraction(x, y)

    # 减法
    def __sub__(self, other):
        x = self.num*other.den - self.den*other.num
        y = self.den * other.den

        return Fraction(x, y)

    #  乘法
    def __mul__(self, other):
        x = self.num * other.num
        y = self.den * other.den
        return Fraction(x, y)

    # 对应除法（ / ）
    def __truediv__(self, other):
        x = self.num * other.den
        y = self.den * other.num

        # 分子、分母 有一个是负数
        if (x < 0 and y >= 0) or (x >= 0 and y < 0):
            return Fraction(-(abs(x)), abs(y))
        else:
            return Fraction(x, y)


def gcd(x, y):
    # x,y 必须都是自然数
    if x < y:
        x, y = y, x
    while y != 0:
        temp = x
        x = y
        y = temp % y
    return x


if __name__ == '__main__':
    start = time.perf_counter()

    x, y = input().split(" ")
    a1, b1 = tuple(map(int, x.split("/")))
    a2, b2 = tuple(map(int, y.split("/")))

    x = Fraction(a1, b1)
    y = Fraction(a2, b2)

    print(x.show(), "+", y.show(), "=", (x + y).show())
    print(x.show(), "-", y.show(), "=", (x - y).show())
    print(x.show(), "*", y.show(), "=", (x * y).show())
    print(x.show(), "/", y.show(), "=", (x / y).show())

    end = time.perf_counter()
    print(end - start)
