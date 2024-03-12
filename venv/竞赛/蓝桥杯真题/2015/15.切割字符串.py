# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/11 10:52'

def is_palindrome(string):  # 判断是否是正回文子串
    length = len(string)
    if length % 2 == 1:  # 仅比正常比较回文串多出一步判断长度
        for y in range(length // 2):
            if string[y] != string[length - y - 1]:
                return False
        return True
    else:
        return False


n = int(input().strip())
string = input().strip()
A_is_palindrome_list = []
B_not_palindrome_list = []

# 遍历所有切法
for i in range(1, n):
    A_is_exit = []
    B_is_exit = []
    A = string[:i]
    B = string[i:]
    # print(A, B)
    A_length = len(A)
    B_length = len(B)
    count = 0
    # 遍历所有A和B的子串
    for p in range(1, A_length + 1):  # 子串长度
        for q in range(A_length - p + 1):  # 起始位置
            if is_palindrome(A[q:q + p]):
                if A[q:q + p] not in A_is_exit:  # 是否已经出现过
                    A_is_exit.append(A[q:q + p])
                    count += 1
                else:
                    continue
    A_is_palindrome_list.append(count)
    # print(A_is_palindrome_list)
    count = 0
    for p in range(1, B_length + 1):  # 子串长度
        for q in range(B_length - p + 1):  # 起始位置
            if not is_palindrome(B[q:q + p]):
                if B[q:q + p] not in B_is_exit:
                    B_is_exit.append(B[q:q + p])
                    count += 1
                else:
                    continue
    # print(count)
    B_not_palindrome_list.append(count)
    # print(B_not_palindrome_list)
result = max(map((lambda x, y: x * y), A_is_palindrome_list, B_not_palindrome_list))
print(result)