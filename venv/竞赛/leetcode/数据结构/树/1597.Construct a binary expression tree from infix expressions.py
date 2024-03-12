# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/17 15:52'

import time


class Solution:
    # 方法一:弹出栈中优先级高于当前的运算符并计算
    def expTree(self, s: str) -> 'Node':

        def infixToPostfix(infixArray):  # 中缀表达式->后缀表达式
            prior = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}  # 运算符优先级
            size = len(infixArray)
            postfix = []

            stack = []
            i = 0
            while i < size:
                cur_char = infixArray[i]

                if cur_char.isdigit():  # 数字直接入结果栈
                    postfix.append(cur_char)

                # find the last '('
                elif cur_char == ')':  # 遇到右括号,弹出临时栈中当前括号内的所有内容并加入结果栈中
                    while stack[-1] != '(':
                        postfix.append(stack.pop())
                    stack.pop()

                # highest priority, no pop
                elif cur_char == '(':
                    stack.append(cur_char)

                else:
                    while stack and prior[stack[-1]] >= prior[cur_char]:  # 遇到低优先级的运算符,把临时栈中高优先级的运算符加入到结果栈
                        postfix.append(stack.pop())
                    stack.append(cur_char)
                i += 1

            rest = len(stack)

            for i in range(rest):
                postfix.append(stack.pop())

            return postfix

        p = infixToPostfix(s)

        def constructTree(p):
            if not p:
                return None

            cur_node = Node(p.pop())

            if cur_node.val.isdigit():
                return cur_node

            cur_node.right = constructTree(p)
            cur_node.left = constructTree(p)

            return cur_node

        return constructTree(p)


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
