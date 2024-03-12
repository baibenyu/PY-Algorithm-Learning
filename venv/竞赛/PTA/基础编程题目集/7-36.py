# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/5 10:38'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    def complexadd(a1, b1, a2, b2):
        r, v = a1 + a2, b1 + b2
        return r, v


    def complexminus(a1, b1, a2, b2):
        r, v = a1 - a2, b1 - b2
        return r, v


    def complexmul(a1, b1, a2, b2):
        r, v = a1 * a2 - b1 * b2, a1 * b2 + a2 * b1
        return r, v


    def complexdiv(a1, b1, a2, b2):
        r, v = complexmul(a1, b1, a2, -b2)
        r, v = r / (a2 ** 2 + b2 ** 2), v / (a2 ** 2 + b2 ** 2)
        return r, v


    a1, b1, a2, b2 = map(float, input().split())
    # a1, b1, a2, b2 = round(a1, 1), round(b1, 1), round(a2, 1), round(b2, 1)
    op = ["+", "-", "*", "/"]
    for i in range(4):
        if i == 0:
            r, v = complexadd(a1, b1, a2, b2)
        elif i == 1:
            r, v = complexminus(a1, b1, a2, b2)
        elif i == 2:
            r, v = complexmul(a1, b1, a2, b2)
        else:
            r, v = complexdiv(a1, b1, a2, b2)
        r = round(r, 1)
        v = round(v, 1)
        if r == 0 and v == 0:
            print(f"({a1:.1f}{b1:+.1f}i) {op[i]} ({a2:.1f}{b2:+.1f}i) = 0.0")
        elif r == 0:
            print(f"({a1:.1f}{b1:+.1f}i) {op[i]} ({a2:.1f}{b2:+.1f}i) = {v:.1f}i")
        elif v == 0:
            print(f"({a1:.1f}{b1:+.1f}i) {op[i]} ({a2:.1f}{b2:+.1f}i) = {r:.1f}")
        else:
            print(f"({a1:.1f}{b1:+.1f}i) {op[i]} ({a2:.1f}{b2:+.1f}i) = {r:.1f}{v:+.1f}i")

    end = time.perf_counter()
    print(end - start)
