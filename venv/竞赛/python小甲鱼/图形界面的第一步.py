import easygui as g
import sys

while 1:
    g.msgbox("墨染希：成功坚持到了对话界面的第一步呢，你很棒了！期待你早日来接我们。")

    msg = "请问你希望在大学学习到什么知识呢？"
    title = "小游戏互动"
    choices = ["谈恋爱", "编程", "人工智能算法", "统计学", "高数"]

    choice = g.choicebox(msg, title, choices)

    # note that we convert choice to string, in case
    # the user cancelled the choice, and we got None.
    g.msgbox("你的选择是: " + str(choice), "结果")

    msg = "你希望重新开始小游戏吗？"
    title = "请选择"

    if g.ccbox(msg, title):  # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:
        sys.exit(0)  # user chose Cancel
