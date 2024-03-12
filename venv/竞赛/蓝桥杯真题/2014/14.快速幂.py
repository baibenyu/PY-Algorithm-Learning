# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/10 20:17'

index = 1000000000
base = 2
result = 1
mod = 1000
while index:
    if int(index) & 1:  # 如果是指数为奇数,则将底数乘入答案中(是根据数学归纳法推导出的结果,与正常计算的结果一致)
        result = result * base % mod
    base = base ** 2 % mod  # 底数变为原来的平方
    index /= 2  # 因为底数每次循环都会变为自己的平方,所以指数应该变为原来的一半
print(result)
