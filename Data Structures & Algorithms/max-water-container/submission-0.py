import numpy as np
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        water = np.zeros((n, n))
        for i in range(n):
            for j in range(i+1, n):
               water[i, j] = abs(min(heights[j], heights[i]))*(j-i)
        return int(water.max())