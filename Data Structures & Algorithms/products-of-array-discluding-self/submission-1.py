class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        prefix_product_array = [0]*n
        suffix_product_array = [0]*n

        cur_prefix_product = 1
        cur_suffix_product = 1

        for i in range(n):
            prefix_product_array[i] = cur_prefix_product
            suffix_product_array[n-i-1] = cur_suffix_product

            cur_prefix_product *= nums[i]
            cur_suffix_product *=nums[n-i-1]
        
        result = [0]*n

        for i in range(n):
            result[i] = prefix_product_array[i]*suffix_product_array[i]
        
        return result