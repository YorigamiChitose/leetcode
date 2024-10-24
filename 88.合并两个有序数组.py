#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

from typing import List


# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x = m + n
        for i in range(x - 1, -1, -1):
            if m == 0:
                nums1[i] = nums2[n - 1]
                n -= 1
            elif n == 0:
                nums1[i] = nums1[m - 1]
                m -= 1
            else:
                if nums1[m - 1] > nums2[n - 1]:
                    nums1[i] = nums1[m - 1]
                    m -= 1
                else:
                    nums1[i] = nums2[n - 1]
                    n -= 1
# @lc code=end

