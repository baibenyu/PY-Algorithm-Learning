import os
list1 = []

def search_file(start_dir, target):
    os.chdir(start_dir)

    for each in os.listdir(os.curdir):
        if os.path.isdir(each):
            search_file(each,target)
            os.chdir(os.pardir)
        if os.path.splitext(each)[1] == target:
            list1.append(os.getcwd()+os.sep+each+os.linesep)
    return list1
            
start_dir = input('请输入路径：')
target = input('请输入扩展名:')
list1=search_file(start_dir, target)
f = open(os.getcwd()+os.sep+'list.txt','a+')
f.writelines(list1)
f.close()
