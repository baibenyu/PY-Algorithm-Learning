dp = [0 for i in range(1000000)]
count = 0
a, b = map(int, input().split())
dp[a] = dp[b] = 1

for i in range(max(a, b) + 1, 1000000):
    dp[i] = dp[i - a] or dp[i - b]

for i in range(1000000):
    if dp[i] == 0:
        count = i

print(count)
