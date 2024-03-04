# https://leetcode.com/problems/container-with-most-water/description/
# 11. Container With Most Water

# height = [1,8,6,2,5,4,8,3,7]
# output = 49

# height = [1,1]
# output = 1

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        f = 0
        while(l<r):
            f = max(f, (r-l)*min(height[l], height[r]))
            if(height[l]<height[r]):
                l+=1
            else:
                r-=1
        return f
        