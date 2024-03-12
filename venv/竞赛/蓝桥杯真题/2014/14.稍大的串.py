# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/10 19:18'

temp = input().strip()
string = list(temp)
length = len(string)

i = length - 2  # 至少两个元素才能交换,排序
while i >= 0 and string[i] >= string[i + 1]:  # 从后往前找到第一个小于后面元素的a[i]
    i -= 1

if i >= 0:  # 若整个数组为降序,则在a[i]之后不存在比a[i]大的元素,不用执行while
    j = length - 1
    while j >= i and string[j] <= string[i]:  # 从后往前找到第一个大于a[i]的元素
        j -= 1
    string[i], string[j] = string[j], string[i]

left, right = i + 1, length - 1
while left < right:  # 因为原来顺序是降序,将i后的升序排序只需要逆转即可
    string[left], string[right] = string[right], string[left]
    left += 1
    right -= 1
print(string)
