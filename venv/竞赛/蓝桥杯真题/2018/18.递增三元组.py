# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/19 9:07'

import time

start = time.clock()

n, res = int(input()), 0
nums = list(map(lambda in_: sorted(in_),
                [list(map(int, input().split()))[:n] for _ in range(3)]))
# print(*nums, sep='\n')
for i in range(n):
    temp_index_0, temp_index_1 = 0, 0
    # second sequence
    for j in range(temp_index_0, n):
        a, b = 0, 0
        if nums[1][j] > nums[0][i]:
            temp_index_0 = j
            for k in range(temp_index_1, n):
                if nums[2][k] > nums[1][j]:
                    b = n - k
                    temp_index_1 = k
                    res += b
                    break
print(res)

end = time.clock()
print(end - start)
