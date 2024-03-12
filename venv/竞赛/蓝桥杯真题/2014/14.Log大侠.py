# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/9 22:11'
import math

n, m = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))
matrix = []
for i in range(m):
    matrix.append(list(map(int, input().strip().split())))

while matrix:
    temp = matrix.pop(0)
    for i in range(temp[0]-1, temp[1]):
        nums[i] = int(math.log2(nums[i]))+1
    print(sum(nums))
