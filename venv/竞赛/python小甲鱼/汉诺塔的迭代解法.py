def fabol(n):
    print("从左到右柱子依次为ABC，最底下为第一号")
    odd = ['C', 'B', 'A']  # 把二到五层汉诺塔列出来后发现奇数层的行动循环
    double = ['B', 'C', 'A']  # 偶数层的行动循环
    while n > 0:
        num = 2 ** (n - 1)  # 每层的行动总数
        multiple = num // 3
        remainder = num % 3
        if n == 1:
            print("第", n, "号盘的全部行动:", ['C'])
        elif n % 2 == 1:  # 判断是否是奇数层
            temp = multiple * odd + odd[:remainder]
            print("第", n, "号盘的全部行动:", temp)
        else:  # 偶数层
            temp = multiple * double + double[:remainder]
            print("第", n, "号盘的全部行动:", temp)
        n -= 1
    print("以杨辉三角形式依次从第一号盘开始，行动分别单个插入到下一号盘的相邻行动的中间，最终得到解法")
