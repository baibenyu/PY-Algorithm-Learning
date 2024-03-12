import math

# 将题目转化为求最小公倍数=a*b//最大公约数
a, b, c = map(int, input().strip().split())

b = (a * b) // math.gcd(a, b)
ans = b * c // math.gcd(b, c)

print(ans)
