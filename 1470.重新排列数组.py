#
# @lc app=leetcode.cn id=1470 lang=python3
#
# [1470] 重新排列数组
#

from typing import List


# @lc code=start
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [nums[i // 2 + (i % 2) * n] for i in range(2 * n)]
# @lc code=end

