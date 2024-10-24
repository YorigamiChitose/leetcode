#
# @lc app=leetcode.cn id=1281 lang=python3
#
# [1281] 整数的各位积和之差
#

# @lc code=start
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        j = 1
        h = 0
        for i in n:
            j *= int(i)
        for i in n:
            h += int(i)
        return j - h
# @lc code=end

