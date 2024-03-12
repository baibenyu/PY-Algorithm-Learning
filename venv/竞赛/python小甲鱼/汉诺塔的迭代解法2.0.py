def fabol(n, lst=[]):
    print("从左到右柱子依次为ABC，最底下为第一号")
    odd = ['C', 'B', 'A']  # 把二到五层汉诺塔列出来后发现了奇数层的行动循环
    double = ['B', 'C', 'A']  # 偶数层的行动循环
    while n > 0:
        num = 2 ** (n - 1)  # 每层的行动总数
        multiple = num // 3  # 倍数
        remainder = num % 3  # 余数
        if n == 1:
            # print("第",n,"号盘的全部行动:",['C'])
            lst.append(['C'])
        elif n % 2 == 1:  # 判断是否是奇数层
            temp = multiple * odd + odd[:remainder]
            # print("第",n,"号盘的全部行动:",temp)
            lst.append(temp)
        else:  # 偶数层
            temp = multiple * double + double[:remainder]
            # print("第",n,"号盘的全部行动:",temp)
            lst.append(temp)
        n -= 1
    print("以杨辉三角形式依次从第一号盘开始，行动分别单个插入到下一号盘的相邻行动的中间，直到最后一号盘，最终得到解法")
    lst2 = lst[::-1]
    lst.clear()
    for i in range(len(lst2)):
        for j in range(len(lst2[i]) - 1):
            lst2[i].insert(j * 2 + 1, lst2[i - 1][j])
    return lst2[-1]
