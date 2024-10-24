#
# @lc app=leetcode.cn id=1422 lang=python3
#
# [1422] 分割字符串的最大得分
#

# @lc code=start
class Solution:
    def maxScore(self, s: str) -> int:
        max_ans = 0
        for i in range(0, len(s) - 1):
            max_ans = max(max_ans, s[:i + 1].count('0') + s[i + 1:].count('1'))
        return max_ans

# @lc code=end
