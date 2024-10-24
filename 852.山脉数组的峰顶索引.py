#
# @lc app=leetcode.cn id=852 lang=python3
#
# [852] 山脉数组的峰顶索引
#

from typing import List


# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # return arr.index(max(arr))
        l, r = 1, len(arr) - 1

        while(l < r):
            mid = (l + r + 1) >> 1

            if (arr[mid - 1] < arr[mid]):
                l = mid
            else:
                r = mid - 1
        return r
# @lc code=end

