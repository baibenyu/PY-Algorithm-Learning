# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/6 11:30'

class ListNode:
    def __init__(self, coef, exp):
        self.coef = coef
        self.exp = exp
        self.next = None


def list2LinkList(lst):
    if lst[0] == 0:
        return 0
    head = ListNode(0, 0)
    tail = head
    for i in range(1, len(lst), 2):
        node = ListNode(lst[i], lst[i + 1])
        # print(node.coef,node.expon)
        tail.next = node
        tail = node
    return head.next


def add(lst1, lst2):
    h1 = lst1
    h2 = lst2
    addRes = []
    while h1 and h2:
        e1 = h1.exp
        e2 = h2.exp
        if e1 < e2:
            if h2.coef != 0:
                addRes.append(h2.coef)
                addRes.append(e2)
            h2 = h2.next
        elif e1 > e2:
            if h1.coef != 0:
                addRes.append(h1.coef)
                addRes.append(e1)
            h1 = h1.next
        else:
            if (h1.coef + h2.coef) != 0:
                addRes.append(h1.coef + h2.coef)
                addRes.append(e1)
            h1 = h1.next
            h2 = h2.next
    while h1:
        if h1.coef != 0:
            addRes.append(h1.coef)
            addRes.append(h1.exp)
        h1 = h1.next
    while h2:
        if h2.coef != 0:
            addRes.append(h2.coef)
            addRes.append(h2.exp)
        h2 = h2.next
    return [0, 0] if len(addRes) == 0 else addRes


def mul(lst1, lst2):
    h1 = lst1
    h2 = lst2
    p = ListNode(0, 0)
    tail = p
    while h2:  # lst1的第一项乘以lst2的每一项，得到p
        node = ListNode(h1.coef * h2.coef, h1.exp + h2.exp)
        tail.next = node
        tail = node
        h2 = h2.next
    h1 = h1.next
    while h1:  # lst1第一项之后的每一项都与lst2的每一项相乘
        h2 = lst2
        tail = p
        while h2:
            c = h1.coef * h2.coef
            e = h1.exp + h2.exp
            # print(c,e)
            while tail.next and tail.next.exp > e:  # 寻找插入的位置
                tail = tail.next
            if tail.next and tail.next.exp == e:
                if tail.next.coef + c != 0:
                    tail.next.coef += c
                else:
                    tail.next = tail.next.next
            else:
                t = ListNode(c, e)
                t.next = tail.next
                tail.next = t
                tail = tail.next

            h2 = h2.next

        h1 = h1.next
    mulRes = []
    p = p.next
    while p:
        if p.coef != 0:
            mulRes.append(p.coef)
            mulRes.append(p.exp)
        p = p.next
    return [0, 0] if len(mulRes) == 0 else mulRes


def printFun(lst):
    ls = [str(i) for i in lst]
    print(' '.join(ls))


# 输入
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
if len(lst1) == 1 and len(lst2) == 1:
    printFun([0, 0])
    printFun([0, 0])
elif len(lst1) == 1 and len(lst2) > 1:
    printFun([0, 0])
    printFun(lst2[1:])
elif len(lst1) > 1 and len(lst2) == 1:
    printFun([0, 0])
    printFun(lst1[1:])
else:
    L1 = list2LinkList(lst1)
    L2 = list2LinkList(lst2)
    printFun(mul(L1, L2))
    printFun(add(L1, L2))
