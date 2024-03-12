def huiwen(temp, start, end):
    if start > end:
        return 1
    else:
        if temp[start] == temp[end]:
            return huiwen(temp, start + 1, end - 1)
        else:
            0


temp = input('请输入一段文字：')
length = len(temp)
end = length - 1
if huiwen(temp, 0, end):
    print('%s是一个回文字符串！' % temp)
else:
    print('%s不是一个回文字符串！' % temp)
