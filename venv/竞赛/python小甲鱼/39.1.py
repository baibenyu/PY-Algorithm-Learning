class Stack:
    list1 = []
    list1_len = len(list1)

    def isEmpty(self):
        if self.list1 == []:
            return True
        else:
            return False

    def push(self,x):
        self.list1.append(x)

    def pop(self):
        return self.list1.pop()

    def top(self):
        return self.list1[self.list1_len-1]

    def botton(self):
        return self.list1[0]



s = Stack()
s.push(2)
s.push(3)
print(s.list1)
print(s.top())
print(s.botton())
print(s.pop())