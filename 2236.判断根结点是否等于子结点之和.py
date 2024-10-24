#
# @lc app=leetcode.cn id=2236 lang=python3
#
# [2236] 判断根结点是否等于子结点之和
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right

from typing import Optional


# @lc code=start
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val == (root.right.val + root.left.val)
# @lc code=end

