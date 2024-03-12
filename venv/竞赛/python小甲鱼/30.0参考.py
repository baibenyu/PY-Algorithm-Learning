import os

all_files = os.listdir(os.curdir)  # 使用os.curdir表示当前目录更标准
type_dict = dict()  # 先定一个空字典来存放{'后缀名': 数量}

for each_file in all_files:
    if os.path.isdir(each_file):
        type_dict.setdefault('文件夹', 0)  # 当原字典中无该键时，则新增该键和对于的值，并返回键值
        type_dict['文件夹'] += 1
    else:
        ext = os.path.splitext(each_file)[1]  # 返回的是元组，获取文件的后缀名=ext
        type_dict.setdefault(ext, 0)
        type_dict[ext] += 1

for each_type in type_dict.keys():
    print('该文件夹下共有类型为【%s】的文件 %d 个' % (each_type, type_dict[each_type]))
    
        

