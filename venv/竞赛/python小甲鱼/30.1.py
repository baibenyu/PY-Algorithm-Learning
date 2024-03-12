import os
file_name = os.listdir(os.curdir)
for each in file_name:
    if os.path.isfile(each):
        size = os.path.getsize(each)
        print(each,size,'Bytes')
