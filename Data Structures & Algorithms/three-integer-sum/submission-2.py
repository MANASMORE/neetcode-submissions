class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range (len(nums)-2):
            if nums[i] > 0:
                break
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            lf = i+1
            rt = len(nums)-1

            while lf < rt:
                total = nums[i] + nums[lf] + nums[rt]

                if total < 0:
                    lf+=1
                
                elif total > 0:
                    rt-=1

                else:
                    result.append([nums[i],nums[lf],nums[rt]])
                    lf+=1
                    rt-=1

                    while lf < rt and nums[lf] == nums[lf-1]:
                        lf+=1
                    
                    while lf < rt and nums[rt] == nums[rt+1]:
                        rt-=1
        
        return result