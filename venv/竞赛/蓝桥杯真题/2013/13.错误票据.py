import collections
# 找到票据的最小值和最大值来重新生成一个完整的序列,遍历完整的序列在题目所给序列找到缺失的票号
n = int(input())
data = []

for _ in range(n):
    data.extend(list(map(int,input().strip().split())))

maxnum = max(data)
minnum = min(data)
ans = [i for i in range(minnum,maxnum+1)]

for each in ans:
    if each not in data:
        print(each,end = " ")
        break
    
repeat = collections.Counter(data)
print(repeat.most_common(1)[0][0])
