# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/11 10:43'

# 普通的回溯
n = int(input().strip())
matrix = []
flag = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    temp = input().strip().split()
    if "A" in temp:
        A_index = (i, temp.index("A"))
    if "B" in temp:
        B_index = (i, temp.index("B"))
    matrix.append(temp)
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
step = float("inf")


def dfs(position, pas):
    global step
    if position == B_index:
        step = min(step, pas)
        return
    for each in directions:
        dx = position[0] + each[0]
        dy = position[1] + each[1]
        if 0 <= dx < n and 0 <= dy < n and not flag[dx][dy] and matrix[position[0]][position[1]] != matrix[dx][dy]:#必须相反,即不同
            flag[dx][dy] = True
            dfs((dx, dy), pas + 1)
            flag[dx][dy] = False


dfs(A_index, 0)
print(step)