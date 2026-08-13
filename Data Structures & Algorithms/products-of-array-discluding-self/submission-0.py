class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = 1
        right_prod = 1
        ans = [1]*len(nums)

        for i in range(len(nums)):
            ans[i] = left_prod
            left_prod *= nums[i]

        for i in range(len(nums)-1,-1,-1):
            ans[i] *= right_prod
            right_prod *= nums[i]

        return ans