class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for i in nums:

            if i-1 not in num_set:
                count = 1
                while i+1 in num_set:
                    count = count+1
                    i+=1
                
                longest = max(longest, count)
            
        return longest