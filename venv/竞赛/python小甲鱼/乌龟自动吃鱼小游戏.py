import random


class Fish:
    number = 10
    step = 1
    position_list = list()

    def position(self):
        for i in range(self.number):
            x = random.randint(1, 10)
            y = random.randint(1, 10)
            self.position_list.append([x, y])

    def change(self):
        for i in range(self.number):
            turn = random.randint(0, 3)

            if turn == 0:  # 行动逻辑
                x = self.position_list[i][0] + self.step
                y = self.position_list[i][1]
                if x > 10:
                    x = self.position_list[i][0] - self.step
            elif turn == 1:
                x = self.position_list[i][0]
                y = self.position_list[i][1] + self.step
                if y > 10:
                    y = self.position_list[i][1] - self.step
            elif turn == 2:
                x = self.position_list[i][0] - self.step
                y = self.position_list[i][1]
                if x < 0:
                    x = self.position_list[i][0] + self.step
            elif turn == 3:
                x = self.position_list[i][0]
                y = self.position_list[i][1] - self.step
                if y < 0:
                    y = self.position_list[i][1] + self.step

            self.position_list[i] = [x, y]


class Tortoise:
    position_list = list()
    strength = 100

    def position(self):
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        self.position_list.append([x, y])

    def change(self):
        turn = random.randint(0, 3)
        step = random.randint(1, 2)

        if turn == 0:  # 行动逻辑
            x = self.position_list[0][0] + step
            y = self.position_list[0][1]
            if x > 10:
                x = self.position_list[0][0] - step
        elif turn == 1:
            x = self.position_list[0][0]
            y = self.position_list[0][1] + step
            if y > 10:
                y = self.position_list[0][1] - step
        elif turn == 2:
            x = self.position_list[0][0] - step
            y = self.position_list[0][1]
            if x < 0:
                x = self.position_list[0][0] + step
        elif turn == 3:
            x = self.position_list[0][0]
            y = self.position_list[0][1] - step
            if y < 0:
                y = self.position_list[0][1] + step

        self.position_list[0] = [x, y]
        self.strength -= 1

    def eating(self):

        if self.position_list[0] in Fish.position_list:
            count = Fish.position_list.count(self.position_list[0])
            print("乌龟在", self.position_list[0], "位置吃掉了%d只鱼" % count)
            Fish.position_list.remove(self.position_list[0])
            Fish.number -= count
            self.strength += count * 20
            if self.strength > 100:
                self.strength = 100


print("欢迎进入乌龟吃鱼小游戏!")
A = Fish()
B = Tortoise()
A.position()
B.position()
while A.position_list != [] and B.strength != 0:
    B.eating()
    A.change()
    B.change()
    B.eating()
if not A.position_list:
    print("鱼被吃完啦!好厉害的乌龟???")
if B.strength == 0:
    print("好菜的乌龟,不行啊,还得继续努力!")
