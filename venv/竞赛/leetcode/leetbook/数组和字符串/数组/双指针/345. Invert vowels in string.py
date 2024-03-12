# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/19 9:34'

import time


class Solution:
    # 方法一:双指针--对撞指针
    def reverseVowels(self, s: str) -> str:
        vowels = {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"}
        i, j = 0, len(s) - 1
        string = list(s)
        while i < j:
            while i < j and s[i] not in vowels:
                i += 1
            while i < j and s[j] not in vowels:
                j -= 1
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1
        return "".join(string)


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
