def hanoi(n, x, y, z):
    if n == 1:
        print(x, '->', z)
    else:
        hanoi(n - 1, x, z, y)  # 将x上的前n-1个盘移动到y上
        print(x, '->', z)  # 将x上的n盘移动到z上
        hanoi(n - 1, y, x, z)  # 将y盘上的n-1个盘移动到z上


n = int(input('请输入汉诺塔的层数：'))
hanoi(n, 'X', 'Y', 'Z')
