# 第一种方法：
f1 = open('D:\Python\Python3\OpenMe.mp3')
f2 = open('D:\Python\Python3\OpenMe.txt','x')
for each_line in f1:
    f2.write(each_line)
f1.close()
f2.close()

#第二种方法
f1 = open('D:\Python\Python3\OpenMe.mp3')
f2 = open('D:\Python\Python3\OpenMe2.txt','x')
f2.write(f1.read())
f1.close()
f2.close() 
