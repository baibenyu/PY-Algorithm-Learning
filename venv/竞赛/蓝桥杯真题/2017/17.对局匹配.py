# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/16 21:09'

import time

start = time.clock()
import collections

n, k = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))
count = collections.Counter(nums)
weight = [[float("-inf"), 0, 0, 0] for _ in range(200001)]
flag = [True for _ in range(200001)]
if k == 0:
    print(len(set(nums)))
else:
    for each in count.keys():
        weight[each][0] = count[each] - count[each + k] - count[each - k]
        weight[each][1] = each
        weight[each][2] = each - k
        weight[each][3] = each + k
    weight.sort(key = lambda x: x[0], reverse = True)
    max_num = 0
    for i in range(len(weight)):
        if weight[i][0] == float("-inf"):
            break
        if flag[weight[i][1]]:
            max_num += count[weight[i][1]]
            flag[weight[i][2]], flag[weight[i][3]] = False, False
    print(max_num)
end = time.clock()
print(end - start)
