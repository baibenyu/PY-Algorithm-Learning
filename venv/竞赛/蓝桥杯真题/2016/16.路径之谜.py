# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/14 10:00'

import time


# 暴力回溯+剪枝
def dfs(position, pas):
    global ans
    if position == (n - 1, n - 1):
        if sum(c_count) == 0 and sum(r_count) == 0:
            ans = pas.copy()
        return
    else:
        for each in directions:
            dx = position[0] + each[0]
            dy = position[1] + each[1]
            if 0 <= dx < n and 0 <= dy < n and not matrix[dx][dy]:
                c_count[dy] -= 1  # 行列剩余还需经过的次数
                r_count[dx] -= 1
                if c_count[dy] < 0 or r_count[dx] < 0:
                    c_count[dy] += 1
                    r_count[dx] += 1
                    continue
                matrix[dx][dy] = 1
                pas.append((dx, dy))
                dfs((dx, dy), pas)
                c_count[dy] += 1
                r_count[dx] += 1
                matrix[dx][dy] = 0
                pas.pop()


n = int(input().strip())
c_count = list(map(int, input().strip().split()))
r_count = list(map(int, input().strip().split()))
start = time.clock()
ans = []
matrix = [[0 for _ in range(n)] for _ in range(n)]  # 是否走过坐标
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
c_count[0] -= 1
r_count[0] -= 1
dfs((0, 0), [(0, 0)])
for each in ans:
    print(each[0] * n + each[1], end = " ")
end = time.clock()
print(end - start)
