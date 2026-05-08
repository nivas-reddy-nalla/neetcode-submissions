class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_ = {}

        for idx, val in enumerate(nums):
            if val in map_:
                return [map_[val], idx]
            else:
                map_[target-val] = idx
        return [-1, -1]