# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/6 21:18'

while True:
    n = int(input().strip())

    matrix = []
    for i in range(n):
        matrix.extend(list(map(int, input().strip().split())))

    for p in range(n):
        count_0 = 0
        count_1 = 0
        for q in range(n):
            if matrix[p + q * n] == 0:
                count_0 += 1
            else:
                count_1 += 1
        if count_1 > count_0:
            print(p+1, end = " ")
