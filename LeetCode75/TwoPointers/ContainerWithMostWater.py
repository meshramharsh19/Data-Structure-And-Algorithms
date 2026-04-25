class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            h = min(height[left], height[right])
            distance = right - left
            area = h * distance

            # Move the smaller pointer
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

            # Update maximum area
            if area > max_area:
                max_area = area

        return max_area
