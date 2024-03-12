# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/6/7 20:13'

import time


class MyHashMap:
    # 方法一:不定拉链法
    def __init__(self):
        self.buckets = 1009
        self.table = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets

    def put(self, key: int, value: int) -> None:
        hashkey = self.hash(key)
        for item in self.table[hashkey]:
            if item[0] == key:
                item[1] = value
                return
        self.table[hashkey].append([key, value])

    def get(self, key: int) -> int:
        hashkey = self.hash(key)
        for item in self.table[hashkey]:
            if item[0] == key:
                return item[1]
        return -1

    def remove(self, key: int) -> None:
        hashkey = self.hash(key)
        for i, item in enumerate(self.table[hashkey]):
            if item[0] == key:
                self.table[hashkey].pop(i)
                return


if __name__ == '__main__':
    start = time.perf_counter()
    """
    1.认识哈希函数及哈希表扩容策略
    解:当遇到数据量过大且数据重复次数小时,可以人为地分组(%),将应该存在key中的数据,存到value中去,充分利用空间
    当遇到链表长度等于logn时,就整体翻倍扩容,哈希表理论实现性能是logn,但工程上可优化至接近O(1)
    2.设计randompool,等概率的返回key值
    解:使用双哈希表,记录索引和值互相映射,删除时用最后一条记录覆盖被删除的记录,保证随机返回key值时随机
    3.布隆过滤器--集合不删除
    解:创建一个bits数组,长度为m,使用k种哈希函数,每个key都对k种哈希,得出k种相应值,再%m得出一个位于0-m-1之间的数,涂黑bits数组中对应的位,
    判断是否在黑名单,同理看k种哈希后对应值是否均涂过.m值越大,失误越小.哈希函数个数要适当.
    n = 样本量;p = 失误率;m = -(n*lnp)/(ln2)**2 空间大小(bit);k = ln2*(m/n) = 0.7*(m/n) 哈希函数个数
    p真 = (1-e^(-(n*k真)/m真))^k真
    4.一致性哈希原理
    解:哈希表选择key时,应该根据访问频率平均分配,
    底层多台服务器分配数据时,每台在哈希结果范围内设置等量虚拟节点,虚拟节点内顺时针的数据归属于对应的服务器,增减服务器时,服务器的负载都是均衡变化,
    不存在单台服务器超载而其它服务器围观,同理虚拟节点的数量能调节各服务器的负载水平
    5.大数据处理
    解:[1]分段范围区域性统计
    [2]哈希函数分类
    [3]位图
    """
    end = time.perf_counter()
    print(end - start)
