#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除有序数组中的重复项 II
#

from typing import List


# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        t = 0
        s = {}
        for i in range(len(nums)):
            if nums[i] in s and s[nums[i]] == 2:
                continue
            else:
                if not nums[i] in s:
                    s[nums[i]] = 1
                else:
                    s[nums[i]] += 1
                nums[t] = nums[i]
                t += 1
        return t
# @lc code=end

