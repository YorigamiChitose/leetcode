#
# @lc app=leetcode.cn id=274 lang=python3
#
# [274] H 指数
#

from typing import List


# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        ans = 0
        for i in range(len(citations)):
            if citations[i] >= len(citations) - i:
                ans = max(ans, len(citations) - i)
        return ans
# @lc code=end
Solution.hIndex(Solution, [3,0,6,1,5])
