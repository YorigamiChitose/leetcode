#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3 的幂
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i = 1;
        while i < n:
            i *= 3
        return i == n;
# @lc code=end

