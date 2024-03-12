def file_replace(file_name,oldword,newword):
    f = open(file_name)
    count = 0
    string = f.read()
    string.replace('\n','')
    f.seek(0,0)
    f.close()
    for each in string:
        if oldword == each:
            count += 1
    print('文件%s中共有%s个%s' %(file_name,count,oldword))
    temp = input('您确定要将所有的%s替换为%s吗？ \n 【Yes\\No】' %(oldword,newword))
    if temp in ['yes','YES','Yes']:
        string.replace(oldword,newword)
        f_new = open(file_name,'w')
        f_new.write(string)
        f_new.close()
    
    f.close()


file_name = input(r'请输入要打开的文件（C:\\test.txt）：')
oldword = input('请输入要替换的字符：')
newword = input('请输入新的单词：')
file_replace(file_name,oldword,newword)
