# https://leetcode.com/problems/contains-duplicate/
# 217. Contains Duplicate

#nums = [1,2,3,1]
#output = True

#nums = [1,2,3,4]
#output = False

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i not in hashset:
                hashset.add(i)
            else:
                return True
        return False