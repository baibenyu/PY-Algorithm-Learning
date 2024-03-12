# 模拟算法描述的过程
m, n = map(int, input().strip().split())
temp = [i for i in range(1, n)]
begin = 1  # 对lucky=2情况,特殊处理
length = len(temp)
lucky = temp[begin]
index = lucky - 1

while index < length:
    temp.pop(index)
    index += lucky - 1  # 每次都会减少一个元素,下标相应也要减少
    length -= 1  # 长度-1
begin = 0

while begin < length - 1:
    begin += 1
    lucky = temp[begin]
    index = lucky - 1

    while index < length:
        temp.pop(index)
        index += lucky - 1
        length -= 1

count = 0
for each in temp:
    if m < each < n:
        count += 1

print(count)
