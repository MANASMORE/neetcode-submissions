class Solution:
    def trap(self, height: List[int]) -> int:
        lf = 0
        rt = len(height) - 1
        lf_max = 0
        rt_max = 0
        res = 0

        while lf < rt:
            if height[lf] <= height[rt]:
                if height[lf] >= lf_max:
                    lf_max = height[lf]
                else:
                    res += lf_max - height[lf]
                lf += 1

            else:
                if height[rt] >= rt_max:
                    rt_max = height[rt]
                else:
                    res += rt_max - height[rt]
                rt -= 1
        
        return res