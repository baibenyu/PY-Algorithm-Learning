n = int(input())
count = 0
se = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}


# 耐心列出所有情况

def check(x, no_used):
    s = str(x)
    cf = set()
    for each in s:
        if each in cf or each not in no_used:  # 自身无重复且未使用已使用的数字
            return 0
        cf.add(each)
    return 1


for i in range(1, n):
    if not check(i, se):
        continue
    used = {x for x in str(i)}
    no_used1 = se - used
    for j in range(1, 10 ** (len(no_used1) // 2)):  # 分母的可能遍历
        if not check(j, no_used1):
            continue
        k = (n - i) * j
        used = {x for x in str(j)}
        no_used2 = no_used1 - used
        if len(no_used2) == len(str(k)) and check(k, no_used2):
            count += 1
print(count)
