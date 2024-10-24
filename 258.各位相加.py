#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        while(num > 9):
            num = str(num)
            ans = 0
            for i in num:
                ans += int(i)
            num = ans
        return num
# @lc code=end

