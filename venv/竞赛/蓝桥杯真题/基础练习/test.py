# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/2 20:23'

n = int(input())
mapL = [list(map(int, input().split())) for _ in range(n)]  # 模拟棋盘
count = 0  # 计数器


def dfs(row, n, s, mapL):  # 参数带入0,n,2,mapl
    global count
    if row == n:  # 判断是否是放完了最后一行，注意我的行数是从0开始，0代表第一行
        if s == 2:  # 2代表黑皇后，3代表白皇后
            dfs(0, n, 3, mapL)  # 黑皇后放完，开始放白皇后
        if s == 3:  # 全部放完
            count += 1
        return
    for i in range(n):
        if mapL[row][i] != 1:  # 不为1、说明放了皇后，或者不能放皇后
            continue
        if check(row, i, s, mapL):  # 参数带入：行，列，某皇后，棋盘
            mapL[row][i] = s  # 可以放，将格子的数字变为放置对应皇后的数字
            dfs(row + 1, n, s, mapL)
            mapL[row][i] = 1  # 回溯


def check(row, j, s, mapL):  # 行，列，某皇后，棋盘
    L = j - row  # 左边对角线列减行都为L
    R = j + row  # 右边对角线列加行都为R
    for i in range(row):
        if mapL[i][j] == s:  # 检查列
            return False
        if L + i >= 0 and mapL[i][L + i] == s:  # 检查左对角线
            return False
        if R - i <= n - 1 and mapL[i][R - i] == s:  # 检查右对角线
            return False
    return True


dfs(0, n, 2, mapL)
print(count)
