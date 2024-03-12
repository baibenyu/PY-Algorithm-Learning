# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/25 22:17'
from typing import List


class Solution:
    # 方法一:堆排序
    # 与第k个最值或前k个最值有关问题,适合用堆(优先队列)结构,设置小根堆的大小为k,即保留nums数组中前k大的数
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heap = []
        for key in nums:
            if len(heap) >= k:  # 堆满后,新的元素要与堆的根结点比较,若大于才能入堆
                if key > heap[0]:
                    heapq.heappushpop(heap, key)
            else:
                heapq.heappush(heap, key)
        return heap[0]

    # 方法二:快排--改快速选择算法
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        def partition(nums: list, left: int, right: int):
            pivot = nums[left]
            begin = left
            i, j = left, right
            while i < j:
                while j > i and nums[j] >= pivot:  # 直到遇到小于目标值的数字才跳下来
                    j -= 1
                while i < j and nums[i] <= pivot:  # 直到遇到大于目标值的数字才停下来
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[i], nums[begin] = nums[begin], nums[i]
            return i

        def quick_select(nums: list, left: int, right: int, k: int):  # 快速选择,因为题目只要第k大的元素,所以只向len-k的下标靠近排序,不必整个数组排序
            cur = partition(nums, left, right)
            if cur == k:
                return
            elif cur < k:
                quick_select(nums, cur + 1, right, k)
            else:
                quick_select(nums, left, cur - 1, k)

        quick_select(nums, 0, len(nums) - 1, len(nums) - k)  # 升序排序,所以第k大的下标=对应长度-k,降序排序的下标=k-1
        return nums[len(nums) - k]


s = Solution()
s.findKthLargest2([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
