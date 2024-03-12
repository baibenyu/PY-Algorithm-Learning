# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/1 10:23'

import time
from typing import List


class Solution:
    # 方法一:回溯
    def letterCasePermutation(self, s: str) -> List[str]:
        # 就两种选择：转换和不转换
        def DFS(path, index):
            if index == len(s):
                res.append(path)
                return
            if s[index].isdigit():  # 是数字，直接加进去
                DFS(path + s[index], index + 1)
            else:  # 是字母
                # 转
                if s[index].islower():  # 小写转大写
                    DFS(path + s[index].upper(), index + 1)
                else:  # 大写转小写
                    DFS(path + s[index].lower(), index + 1)
                # 不转
                DFS(path + s[index], index + 1)

        res = []
        DFS("", 0)
        return res


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
