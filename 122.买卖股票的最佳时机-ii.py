#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

from typing import List


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        all = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                all += prices[i] - prices[i - 1]
        return all
# @lc code=end

