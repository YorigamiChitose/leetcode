#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
#

from typing import List


# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
# @lc code=end

