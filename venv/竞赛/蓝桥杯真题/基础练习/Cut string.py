# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/8 15:07'

def is_palindrome(string):
    length = len(string)
    if length % 2 == 1:
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


for i in range(1, n):
    A_is_exit = []
    B_is_exit = []
    A = string[:i]
    B = string[i:]
    # print(A, B)
    A_length = len(A)
    B_length = len(B)
    count = 0
    for p in range(1, A_length + 1):  # 子串长度
        for q in range(A_length - p + 1):  # 起始位置
            if is_palindrome(A[q:q + p]):
                if A[q:q + p] not in A_is_exit:
                    A_is_exit.append(A[q:q + p])
                    count += 1
                else:
                    continue
    A_is_palindrome_list.append(count)
    # print(A_is_palindrome_list)
    count = 0
    all_sub = 0
    for p in range(1, B_length + 1):  # 子串长度
        for q in range(B_length - p + 1):  # 起始位置
            all_sub += 1
            if not is_palindrome(B[q:q + p]):
                if B[q:q + p] not in B_is_exit:
                    B_is_exit.append(B[q:q + p])
                    count += 1
                else:
                    continue
    # print(all_sub, count)
    B_not_palindrome_list.append(count)
    # print(B_not_palindrome_list)
result = max(map((lambda x, y: x * y), A_is_palindrome_list, B_not_palindrome_list))
print(result)
