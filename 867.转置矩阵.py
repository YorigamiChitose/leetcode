#
# @lc app=leetcode.cn id=867 lang=python3
#
# [867] 转置矩阵
#

from typing import List


# @lc code=start
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
# @lc code=end

