class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = set()
        for i in range(n-2):
            target = -nums[i]

            start, end = i+1, n-1

            while start<end:
                if nums[start]+nums[end] == target:
                    result.add((nums[i], nums[start], nums[end]))
                    start+=1
                    end-=1
                elif nums[start]+nums[end] > target:
                    end-=1
                else:
                    start +=1
        return list(result)
