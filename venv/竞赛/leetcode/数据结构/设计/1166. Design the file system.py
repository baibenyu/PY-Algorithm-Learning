# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/20 15:34'

import time


class FileSystem:

    def __init__(self):
        self.path = set()
        self.hashmap = {}

    def createPath(self, path: str, value: int) -> bool:
        # 判断是否合法
        if len(path) <= 1 or path in self.hashmap.keys():
            return False
        i = 1
        while i < len(path) and path[i] != '/':
            i += 1
        # 不存在子路径
        if i == len(path):
            if path not in self.path:
                self.path.add(path)
                self.hashmap[path] = value
                return True
            else:
                return False
        else:
            for k in range(len(path) - 1, -1, -1):
                if path[k] == '/':
                    break
            s = path[0:k]
            if s in self.path:  # 判断是否存在父路径
                self.hashmap[path] = value
                self.path.add(path)
                return True
            else:
                return False

    def get(self, path: str) -> int:
        if path not in self.hashmap.keys():
            return -1
        return self.hashmap[path]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
