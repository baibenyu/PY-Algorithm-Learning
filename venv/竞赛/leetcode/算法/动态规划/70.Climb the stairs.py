# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/24 22:39'

class Solution:
    # 一和二方法:子问题与原问题之间的规律仍然相同
    # 方法一:递归--记忆化搜索--自顶向下,让原问题在递的过程分解成子问题,在归的过程存储子问题答案,减少冗余计算,并推出原问题的答案
    def climbStairs(self, n: int) -> int:

        def dfs(now: int, memory: list):
            if now == 1 or now == 0:
                return 1
            if memory[now] == -1:  # -1说明该级台阶尚未计算过
                memory[now] = dfs(now - 1, memory) + dfs(now - 2, memory)  # 将当前阶数的可能方案数存入memory数组
            return memory[now]

        memory = [-1] * (n + 1)
        return dfs(n, memory)

    # 方法二:动态规划--自底向上,从子问题的答案直接递推出原问题的答案,
    def climbStairs2(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]
