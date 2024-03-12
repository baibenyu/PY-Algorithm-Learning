# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/5 15:27'

while True:
    # try:
    row, column = map(int, input().strip().split())
    list1 = []

    for i in range(row):
        list1.extend(list(map(int, input().strip().split())))

    r, c = 0, 0  # 标记当前位置
    pattern = 0
    r_higher, r_lower, c_higher, c_lower = row - 1, 0, column - 1, 0

    while r_higher >= r_lower and c_higher >= c_lower:
        if pattern == 0:
            while r <= r_higher:
                print(list1[r * column + c], end = " ")
                r += 1
            pattern = (pattern + 1) % 4  # 四种走向,下->右->上->左
            c_lower += 1  # 列下限+1
            c += 1  # 列+1
            r -= 1  # 行多加了一次,减回去

        elif pattern == 1:
            while c <= c_higher:
                print(list1[r * column + c], end = " ")
                c += 1
            pattern = (pattern + 1) % 4  # 四种走向,下->右->上->左
            r_higher -= 1
            r -= 1
            c -= 1

        elif pattern == 2:
            while r >= r_lower:
                print(list1[r * column + c], end = " ")
                r -= 1
            pattern = (pattern + 1) % 4  # 四种走向,下->右->上->左
            c_higher -= 1
            c -= 1
            r += 1

        elif pattern == 3:
            while c >= c_lower:
                print(list1[r * column + c], end = " ")
                c -= 1
            pattern = (pattern + 1) % 4  # 四种走向,下->右->上->左
            r_lower += 1
            r += 1
            c += 1

# except BaseException as e:
#     print(e)
