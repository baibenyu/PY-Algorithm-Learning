# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/25 15:03'
import collections
import time


class FreqStack(object):
    # 方法一:哈希表存储频率,利用栈后入先出的特性实现频率相等情况下,找到最近访问的数字(最接近栈顶的元素)
    def __init__(self):
        self.freq = collections.Counter()
        self.group = collections.defaultdict(list)
        self.maxfreq = 0

    def push(self, x):
        f = self.freq[x] + 1
        self.freq[x] = f
        if f > self.maxfreq:
            self.maxfreq = f
        self.group[f].append(x)

    def pop(self):
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return x


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
