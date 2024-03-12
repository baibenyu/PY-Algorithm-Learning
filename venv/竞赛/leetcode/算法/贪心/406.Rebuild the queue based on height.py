# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/17 19:13'
from typing import List


class Solution:
    # 方法一:根据高度降序排序,根据前面排了i个大于等于h高度升序排序,然后依次插入数组中就能得到排序好的数组
    # 矮的人不影响高的人在数组中的相对位置,但矮的人在数组中的相对位置受高的人的影响,所以在高的人确定下来之前,矮人的确切位置无法确定,所以应该从高到矮降序排序,在根据前面有几人来确定相同高度的人的相对位置
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        for p in people:
            if len(res) <= p[1]:  # 大于数组长度就在尾部插入
                res.append(p)
            elif len(res) > p[1]:
                res.insert(p[1], p)
        return res

    # 方法二:从低到高排序
    # 每个人在数组中的位置都是确定的,虽然此时我们还不知道,但位置都是固定好的,我们先将矮的人排序,为什么这么做呢?因为最矮的人对应的ki即所谓大于等于自己高度的人数是数组空位中的绝对下标(即对应于结果数组的下标),当最矮的人排完序后,第二矮的人就成了最矮的人,同理将人排在空位中的ki个位置,如此直至排完所有人
    def reconstructQueue2(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (x[0], -x[1]))
        n = len(people)
        ans = [[] for _ in range(n)]
        for person in people:
            spaces = person[1] + 1
            for i in range(n):
                if not ans[i]:
                    spaces -= 1
                    if spaces == 0:
                        ans[i] = person
                        break
        return ans
