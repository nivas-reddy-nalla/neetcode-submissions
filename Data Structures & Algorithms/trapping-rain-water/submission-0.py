class Solution:
    def trap(self, height: List[int]) -> int:
        total_heights = len(height)

        if total_heights == 0:
            return 0
        left_max_height = [0] * total_heights
        right_max_height = [0] * total_heights

        left_max_height[0] = height[0]
        for i in range(1, total_heights):
            left_max_height[i] = max(left_max_height[i-1], height[i])

        right_max_height[total_heights-1] = height[total_heights-1]
        for i in range(total_heights - 2, -1, -1):
            right_max_height[i] = max(right_max_height[i+1], height[i])
        
        result = 0

        for i in range(total_heights):
            result += min(left_max_height[i], right_max_height[i]) - height[i]
        
        return result
