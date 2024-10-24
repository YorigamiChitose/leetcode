#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

from typing import List


# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == 0:
                flag = False
                for j in range(i - 1, -1, -1):
                    if nums[j] > i - j:
                        flag = True
                        break
                if flag:
                    continue
                else:
                    return False
        return True
# @lc code=end
Solution.canJump(Solution, [2, 0, 0])
