#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

from typing import List


# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        t = 0
        s = {}
        for i in range(len(nums)):
            if nums[i] in s:
                continue
            else:
                s[nums[i]] = 1
                nums[t] = nums[i]
                t += 1
        return t
# @lc code=end
s = Solution
s.removeDuplicates(s, [0,0,1,1,1,2,2,3,3,4])
