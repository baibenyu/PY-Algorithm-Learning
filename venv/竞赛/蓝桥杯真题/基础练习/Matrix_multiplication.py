# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/5 20:58'

n, m = map(int, input().strip().split())
matrix_row = []
matrix_column = []

for i in range(n):
    matrix_row.extend(list(map(int, input().strip().split())))  # 将矩阵以行为存储顺序

if m == 0:
    for a in range(n):
        for b in range(n):
            if a == b:
                print(1, end = " ")
            else:
                print(0, end = " ")
        print()
else:
    for p in range(n):
        for q in range(n):
            matrix_column.append(matrix_row[p + q * n])  # 将矩阵以列为存储顺序重排

    matrix_mul = matrix_row.copy()  # 存储当前矩阵值

    for a in range(m - 1):
        temp = []
        for r in range(n):
            for c in range(n):
                temp.append(sum(
                    list(map(lambda x, y: x * y, matrix_mul[r * n:(r + 1) * n], matrix_column[c * n:(c + 1) * n]))))
        matrix_mul = temp  # 每加一次幂,就更新一次矩阵值
    for r in range(n):
        for c in range(n):
            print(matrix_mul[r * n + c], end = " ")
        print()
