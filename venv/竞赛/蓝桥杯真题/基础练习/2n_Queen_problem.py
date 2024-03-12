# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/3 8:12'

def check(row, column, pattern):
    global white, black, list1
    each = 0
    # print(row)
    if pattern == "white":
        while each <= row:
            if white[each] == column or white[each] + each == row + column or white[each] - each == column - row:
                return False
            elif list1[row * n + column] != 1:
                return False
            each += 1
        return True
    else:
        while each <= row:
            if black[each] == column or black[each] + each == row + column or black[each] - each == column - row:
                return False
            elif list1[row * n + column] != 1:
                return False
            each += 1
        return True


def dfs(row, pattern):
    global white, black, count, n, list1
    # print(row)
    if row == n:
        if pattern == "white":
            dfs(0, "black")
        elif pattern == "black":
            # print(white, black)
            count += 1
        return None
    else:
        if pattern == "white":
            for c in range(n):
                if check(row, c, pattern):
                    white[row] = c
                    list1[row * n + c] = 2
                    # print(white, black, list1)
                    dfs(row + 1, pattern)
                    white[row] = 100
                    list1[row * n + c] = 1
        else:
            for c in range(n):
                if check(row, c, pattern):
                    black[row] = c
                    list1[row * n + c] = 3
                    # print(white, black, list1)
                    dfs(row + 1, pattern)
                    black[row] = 100
                    list1[row * n + c] = 1


n = int(input())
white, black, list1 = [x + 100 for x in range(n)], [x + 100 for x in range(n)], []
count = 0
for i in range(n):
    list1.extend(list(map(int, input().strip().split())))

dfs(0, "white")
print(count)
