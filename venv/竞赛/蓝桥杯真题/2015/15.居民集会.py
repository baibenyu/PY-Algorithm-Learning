# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/12 15:35'

# 回溯法,遍历所有可能,但时间复杂度太高,过不了一个测评
# def backing(index, ins_group):
#     global cost, no_ins
#     if index == 3:
#         ins_group.sort()
#         temp = no_ins.copy()
#         for y in range(1, 4):
#             if y > 1:
#                 for i in range(ins_group[y - 1] + 1, ins_group[y] + 1):
#                     temp[i] = (distance[ins_group[y]] - distance[i]) * check[distance[i]]
#             else:
#                 for i in range(0, ins_group[y] + 1):
#                     temp[i] = (distance[ins_group[y]] - distance[i]) * check[distance[i]]
#         cost = min(cost, sum(temp))
#     else:
#         for x in range(ins_group[-1], length + index - 2):
#             ins_group.append(x)
#             backing(index + 1, ins_group)
#             ins_group.pop()
#
#
# n, l = map(int, input().strip().split())
# check = {}
# distance = []
# for _ in range(n):
#     a, b = map(int, input().strip().split())
#     check[a] = b
#     distance.append(a)
#
# length = len(distance)
# no_ins = []
# for i in range(length):
#     no_ins.append((l - distance[i]) * check[distance[i]])
# cost = float("inf")
# backing(0, [-1])
# print(cost)