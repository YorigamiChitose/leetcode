#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

from typing import List


# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nlen = len(nums)
        a = [1] * nlen
        b = [1] * nlen
        for i in range(1, nlen):
            a[i] = a[i - 1] * nums[i - 1]
        for i in reversed(range(nlen - 1)):
            b[i] = b[i + 1] * nums[i + 1]

        ans = [1] * nlen
        for i in range(nlen):
            ans[i] = a[i] * b[i]
        return ans


        
# @lc code=end
Solution.productExceptSelf(Solution, [4,3,2,1,2])

