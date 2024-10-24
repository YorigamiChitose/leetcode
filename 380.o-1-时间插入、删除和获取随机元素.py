#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] O(1) 时间插入、删除和获取随机元素
#

from random import choice


# @lc code=start
class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.maps = {}

    def insert(self, val: int) -> bool:
        if val in self.nums:
            return False
        self.maps[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.nums:
            return False
        index = self.maps[val]
        self.nums[index] = self.nums[len(self.nums) - 1]
        self.maps[self.nums[len(self.nums) - 1]] = index
        self.nums.pop()
        del self.maps[val]
        return True


    def getRandom(self) -> int:
        return choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

