import os

def findfile(initial_directory,object_file):
    allfile = os.walk(initial_directory)
    list1 = list(allfile)
    for each_tuple in list1:
        if object_file in each_tuple[2]:
            print(each_tuple[0],'\\',object_file)

            
initial_directory = input('请输入待查找的初始目录：')
object_file = input('请输入需要查找的目标文件：')
findfile(initial_directory,object_file)
