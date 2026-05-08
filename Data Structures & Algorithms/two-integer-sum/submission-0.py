class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_idx_map = {}

        for idx, val in enumerate(nums):
            if target-val in val_idx_map:
                return [val_idx_map[target-val], idx]
            val_idx_map[val] = idx
        return [-1, -1]