# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/15 20:59'

import time

start = time.clock()


def play(cnt, cur, next):  # cnt表示剩余球数,cur表示当前取球人拥有的球数是奇数还是偶数,next表示另一个取球人拥有的球数是奇数还是偶数
    if character[cnt][cur][next] is not None:  # 如果已经计算过的情况直接返回,不再重复判断
        return character[cnt][cur][next]
    if cnt < choice[0]:  # 当不能再从cnt中取数时,说明结束了
        if cur & 1 == 1 and next & 1 == 0:  # 如果当前取球人的球数是奇数并且另一个人是偶数
            return "+"  # 胜利
        if cur & 1 == 0 and next & 1 == 1:  # 如果当前取球人的球数是偶数并且另一个人是奇数
            return "-"  # 失败
        return "0"  # 否则就是平局
    tie = False  # 标记是否出现过平局
    for i in range(3):  # 遍历取球的取法
        if choice[i] > cnt:  # 因为之前对choice进行过排序,所以如果小于,后面也不用取了
            break
        res = play(cnt - choice[i], next, cur + choice[i] & 1)  # 剩余球数,取球人进行轮换(一人取一次)
        if res == "-":
            character[cnt][cur][next] = "+"  # 记录结果
            return "+"  # 因为我们对取球人进行了轮换,所以说明原取球人胜利,返回+
        if res == "0":  # 如果不能胜利,就尽量争取平局
            tie = True
    if tie:  # 如果出现过平局
        character[cnt][cur][next] = "0"
        return "0"
    character[cnt][cur][next] = "-"  # 平局也没有的情况才返回-
    return "-"


# 注意!以上都是return,即一旦返回接下来的代码都不会再执行了!!!

choice = list(map(int, input().strip().split()))
choice.sort()
begin = list(map(int, input().strip().split()))
character = [[[None, None] for _ in range(2)] for _ in range(1000)]  # 存储各种取数情况的结果,因为用的方法是记忆化递归

for x in range(len(begin)):  # 打印结果
    print(play(begin[x], 0, 0), end = " ")
end = time.clock()
print(end - start)
