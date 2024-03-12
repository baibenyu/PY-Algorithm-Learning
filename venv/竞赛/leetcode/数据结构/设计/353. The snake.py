# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/29 15:10'

import time


class SnakeGame:
    # 方法一:模拟
    def __init__(self, width: int, height: int, food):
        self.snake = list()
        self.snake.append([0, 0])
        self.head = [0, 0]
        self.foods = food
        self.width = width
        self.height = height
        self.score = 0

    def move(self, direction: str) -> int:
        x, y = self.head
        if direction == 'U':
            x -= 1
        elif direction == 'L':
            y -= 1
        elif direction == 'R':
            y += 1
        elif direction == 'D':
            x += 1
        if x < 0 or y < 0 or x > self.height - 1 or y > self.width - 1:
            return -1

        self.head = [x, y]
        self.snake = [self.head] + self.snake  # 存储蛇的身体占据的坐标
        if self.foods and self.head == self.foods[0]:  # 若还有食物且刚好吃到食物
            self.score += 1
            self.foods = self.foods[1:]
        else:
            self.snake = self.snake[:-1]  # 没有吃到食物,那么因为移动,蛇身体坐标改变,抛弃最后一个
        if self.head in self.snake[1:]:  # 头身相撞
            return -1
        return self.score


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
