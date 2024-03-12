# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/29 16:22'

import time
import random


class Codec:
    """
    URL简化类：将一个长url转化为一个短url（转换后的 URL路径 为6位数的字母或数字）

    转化算法：使用 62 位由大小写字母和数字构成的字符串集合 作为 【62进制位表】，
            可表示的 6位url 数量为 62 ** 6 == 586亿多，几亿次以内的调用不用担心
            字典键冲突，不够用的话可以再增加进制位数。
    """
    _chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    _dict = {}
    _key = ''.join(random.sample(_chars, 6))

    @classmethod
    def get_rand(cls):
        return ''.join(random.sample(cls._chars, 6))

    @classmethod
    def encode(cls, long_url):
        """
        将一个 长URL 编码为一个 短URL【随机固定长度加密】。

        使用 random 模块 随机从 62 位字符串中选取 6 个作为 URL短路径。
        因为使用了随机数，根据 short_url 来预测字典大小几乎是不可能的，数据更加安全。
        """
        while cls._dict.get(cls._key):
            cls._key = cls.get_rand()

        cls._dict[cls._key] = long_url

        return 'http://tinyurl.com/' + cls._key

    @classmethod
    def decode(cls, short_url):
        """
        将一个 短URL 解码为一个 长URL。

        直接根据 url字符串后6位，从字典中取值。
        """
        return cls._dict[short_url[19:]]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
