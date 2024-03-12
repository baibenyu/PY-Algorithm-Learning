def findstr(target,enter):
    times=len(target)-1
    num = 0
    if enter not in target:
        print("未找到字符串")
    else:
        for i in range(times):
            if target[i:i+2] == enter:
                num += 1
            else:
                continue
    return num
    print(num)
target=input('请输入目标字符串:')
enter=input('请输入要查找的两个字符:')
findstr(target,enter)
