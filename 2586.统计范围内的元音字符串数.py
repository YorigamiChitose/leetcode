#
# @lc app=leetcode.cn id=2586 lang=python3
#
# [2586] 统计范围内的元音字符串数
#

from typing import List


# @lc code=start
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        ans = 0
        for s in words[left:right + 1]:
            if s[0] in "aeiou" and s[len(s) - 1] in "aeiou":
                ans += 1
        return ans
# @lc code=end

