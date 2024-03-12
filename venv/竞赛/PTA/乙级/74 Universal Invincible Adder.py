# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/9/24 8:52'

import time

if __name__ == '__main__':
    start = time.perf_counter()

    Basetable = list(input())
    Basetable.reverse()
    a = list(input())
    b = list(input())
    a.reverse()
    b.reverse()
    i = 0
    carry = 0
    ans = []
    while i < len(Basetable):
        tempa, tempb = int(a[i]) if i < len(a) else 0, int(b[i]) if i < len(b) else 0
        cur = int(Basetable[i]) if Basetable[i] != "0" else 10
        ans.append(str((tempa + tempb + carry) % cur))
        carry = (tempa + tempb + carry) // cur
        i += 1

    if carry != 0:
        ans.append(str(carry))
    ans.reverse()
    print(int("".join(ans)))

    end = time.perf_counter()
    print(end - start)
