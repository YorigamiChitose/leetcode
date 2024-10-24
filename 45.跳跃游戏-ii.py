#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

from typing import List


# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        s = 0
        maxPos, end, step = 0, 0, 0
        for i in range(len(nums) - 1):
            if i <= maxPos:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step
            
# @lc code=end

