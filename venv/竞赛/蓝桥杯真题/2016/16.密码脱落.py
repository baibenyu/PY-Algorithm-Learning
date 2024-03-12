# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/14 9:01'

import time

start = time.clock()
# 题目求最少加入几个字符可以使字符串变为回文串,因为回文串是轴对称的,即反转前和反转后应该是一样的,将题目所给字符串反转求最长公共子序列的过程就是在找每个字符在另一边的对称
# 若找到就说明回文串中含有该字符且已在相应位置,剩下找不到对称的字符即为需要在对称的另一边再加一份的字符
string = list(input().strip())
r_string = string.copy()
r_string.reverse()
length = len(string)
dp = [[0 for _ in range(length + 1)] for _ in range(length + 1)]

for i in range(1, length + 1):
    for j in range(1, length + 1):
        if string[i-1] == r_string[j-1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(length-dp[length][length])


end = time.clock()
print(end - start)
