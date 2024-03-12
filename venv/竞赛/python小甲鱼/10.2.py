member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']
member.insert(1,88)
member.insert(3,90)
member.insert(5,85)
member.insert(7,90)
member.append(88)
length=len(member)
for i in range(length):#或者用while语句实现#
    if i%2 == 0:
        print(member[i],member[i+1])
    
