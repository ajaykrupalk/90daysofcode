class Solution:
    def maxArea(self, height):
      l = maxArea = 0
      r = len(height)-1
      while l < r:
        diff = r-l
        minVal = min(height[l],height[r])
        area = diff * minVal
        maxArea = max(maxArea,area)

        if height[l] < height[r]:
          l+=1
        else:
          r-=1
      return maxArea

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))