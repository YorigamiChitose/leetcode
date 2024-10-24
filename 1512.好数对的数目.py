#
# @lc app=leetcode.cn id=1512 lang=python3
#
# [1512] 好数对的数目
#

from typing import List


# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        l = [0] * 101
        ans = 0
        for i in nums:
            ans += l[i]
            l[i] += 1
        return ans

# @lc code=end

