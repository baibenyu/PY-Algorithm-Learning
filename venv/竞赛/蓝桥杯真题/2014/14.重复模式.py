# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/10 19:44'

string = input().strip()
length = len(string)
max_len = float("-inf")
# 参考了另一位笔者的代码,他没有写注释,虽然程序很简短,但细节还是需要思考的,本人只略做修改和注释,方便理解
for i in range(1, length + 1):  # 遍历子串的长度
    for j in range(length - i + 1):  # 遍历起始位置
        if string.find(string[j:j + i], j + 1) != -1 and len(string[j:j + i]) > max_len:
            # 当前起始位置能取到的字符串(出现了一次)能否在起始位置+1之后的部分找到相同的,即出现两次及以上,且长度大于当前最大长度
            max_len = len(string[j:j + i])
        else:  # 此处break思路非常巧妙,代码实际上只求解了每个位置能出现两次的字符串的最大长度,而不是遍历所有的子串,所以平均时间复杂度是要优于O(n**2)
            break
print(max_len)
