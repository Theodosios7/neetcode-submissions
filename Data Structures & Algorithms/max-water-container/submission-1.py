class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Initialize two pointers
        l, r = 0, len(heights) - 1
        max_area = 0
        while l < r:
            width = r - l
            current_height = min(heights[r], heights[l])
            current_area = width * current_height
            # Update maximum area if current area is larger
            max_area = max(max_area, current_area)
            # Move the pointer pointing to the shorter line
            # This is optimal because moving the taller line would never increase the area
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area


