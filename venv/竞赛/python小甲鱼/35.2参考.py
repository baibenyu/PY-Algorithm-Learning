import easygui as e
import os


path = e.fileopenbox(default = "E:/test/*.txt")
with open(path,encoding = "UTF-8") as f:
    text = f.read()
    title = os.path.basename(path)
    msg = "文件%s的内容如下:" % title
    e.textbox(msg,title,text)

