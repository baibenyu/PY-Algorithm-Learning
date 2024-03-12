n, m = map(int, input().strip().split())
# 稀疏图用领接矩阵
matrix = [[0 for x in range(n)] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().strip().split())
    matrix[a - 1][b - 1] = 1
    matrix[b - 1][a - 1] = 1
u, v = map(int, input().strip().split())
u, v = u - 1, v - 1

is_pass = [False for _ in range(n)]
# 有多条路径时,能到达终点的路径上各结点各自被遍历了几次,非必要结点的次数会少于终点(必须)节点的次数
# 即题目要求的关键结点
pass_times = [0 for _ in range(n)]


def dfs(begin, end):
    global pass_times
    if begin == end:
        for i in range(n):
            if is_pass[i]:
                pass_times[i] += 1
        return
    else:
        for j in range(n):
            # 如果存在后续节点且该节点未使用过,移到该节点,继续向终点前进
            if matrix[begin][j] == 1 and not is_pass[j]:
                is_pass[j] = True
                dfs(j, end)  # 并不是每一条路径都一定成功,所以回溯遍历所有路径
                is_pass[j] = False


dfs(u, v)
print(pass_times.count(pass_times[v]) - 1)
