import easygui as e
import os


path = e.fileopenbox(default = "E:/test/*.txt")
with open(path,encoding = "UTF-8") as f:
    previous_text = f.read()
    title = os.path.basename(path)
    msg = "文件%s的内容如下:" % title
    later_text = e.textbox(msg,title,previous_text)


    if previous_text != later_text:
        decision = e.choicebox("检测到文件内容发生改变!请选择是否保存","警告",choices = ["覆盖保存","放弃保存","另存为"])
        if decision != "放弃保存":
            if decision == "覆盖保存":
                with open(path, 'w', encoding = "UTF-8") as f2:
                    f2.write(later_text)
            if decision == "另存为":
                path1 = e.filesavebox(default = path)
                with open(path1, 'w', encoding = "UTF-8") as f1:
                    f1.write(later_text)

