#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

from typing import List


# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp = 0
        for i in range(len(nums)):
            nums[temp] = nums[i]
            if nums[i] != val:
                temp += 1
        return temp
# @lc code=end
s = Solution
s.removeElement(s, [0,1,2,2,3,0,4,2], 2)
