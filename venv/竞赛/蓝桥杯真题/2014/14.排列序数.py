# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/10 19:17'

import itertools
# 暴力法,用permutation生成全排列,然后索引目标的位置
string = input().strip()
temp = list(string)
temp.sort()
ans = list(itertools.permutations(temp))
print(ans.index(tuple(string)))
