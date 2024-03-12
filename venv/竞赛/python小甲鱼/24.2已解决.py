def plalindrome(x):#输入必须是列表！！！不然就返回不是回文
    length = len(x)
    if length == 1:#奇数个的跳出条件
        return '是回文'
    elif length == 2:#偶数个的跳出条件
        if x[0] == x[1]:
            return '是回文'
        else:
            return '不是回文'
    elif x[0] == x[length-1]:#如果相同则向内判断
        return plalindrome(x[1:length-2])
    else:
        return '不是回文'
