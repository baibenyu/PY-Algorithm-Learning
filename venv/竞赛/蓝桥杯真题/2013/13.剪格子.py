# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/8 20:45'

# 模拟算法过程发现,符合深度优先搜索的特性
count = 100  # 记录格子数


def DFS(n, m, map1, vis, total, x, y, xx, yy, ant, sum0):
    """深搜"""
    global count
    if sum0 == total // 2 and count > ant:  # 判断是否当前点的值为总和一半，是一半表示找到了一种方法
        count = ant  # count表示所有方法的最小格子数，ant表示当前方法的格子数
    for i in range(4):  # 模拟当前坐标上下左右的方走
        dx = x + xx[i]
        dy = y + yy[i]
        if 1 <= dx <= m and 1 <= dy <= n and not vis[dx][dy]:
            """dx，dy不能越界并且下一节点没被访问过"""
            vis[dx][dy] = True
            DFS(n, m, map1, vis, total, dx, dy, xx, yy, ant + 1, sum0 + map1[dx][dy])  # 满足条件就格子数加一，和加上当前格子数值
            vis[dx][dy] = False  # 回溯


def main():
    global count
    m, n = map(int, input().split())
    map1 = [[0 for _ in range(m + 2)]] + [[0] + list(map(int, input().split())) + [0] for i in range(n)] + [
        [0 for _ in range(m + 2)]]  # 生成图,关键!!!在外部多包了一层虚拟0,处理了特殊形状的分割
    vis = [[False for i in range(m + 2)] for _ in range(n + 2)]  # 记录每个点是否有没有被访问过
    vis[1][1] = True  # 从坐标1,1开始所以直接令1,1为访问过
    xx = [0, 1, 0, -1]  # x方向的移动
    yy = [1, 0, -1, 0]  # y方向的移动
    total, sum0 = 0, map1[1][1]  # total用来记格子总和，sum0用来记录访问到当前节点的总和值
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            total += map1[i][j]
    if total % 2 == 1:  # 如果总和为奇数这不可能会分为两相等的部分
        print(0)
        return
    DFS(n, m, map1, vis, total, 1, 1, xx, yy, 1, sum0)
    print(0) if count == 100 else print(count)  # 如果count = 100则表示无法分割输出0，否则输出最小格子数


if __name__ == '__main__':
    main()
