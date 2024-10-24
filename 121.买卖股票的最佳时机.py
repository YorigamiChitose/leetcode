#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

from typing import List


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = prices[0]
        maxp = 0
        for i in prices:
            minp = min(i, minp)
            maxp = max(i - minp, maxp)
        return maxp
# @lc code=end
Solution.maxProfit(Solution, [7,1,5,3,6,4])