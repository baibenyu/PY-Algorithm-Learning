# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/9 22:10'

# 模拟题目描述的规则即可
m, n = map(int, input().strip().split())
matrix = []
for i in range(m):
    matrix.append(list(map(int, input().strip().split())))
temp = input().strip().split()
x, y, s, k = int(temp[0]), int(temp[1]), temp[2], int(temp[3])
directions = {"L": [(0, -1), ("D", "U")], "U": [(-1, 0), ("L", "R")], "R": [(0, 1), ("U", "D")],
              "D": [(1, 0), ("R", "L")]}

while k:
    if matrix[x][y] == 0:
        matrix[x][y] = 1
        s = directions[s][1][0]
    else:
        matrix[x][y] = 0
        s = directions[s][1][1]
    if 0 <= x + directions[s][0][0] <= m and 0 <= y + directions[s][0][1] <= n:
        x += directions[s][0][0]
        y += directions[s][0][1]
    k -= 1
print(x, y)
