class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lf = 0
        rt = len(heights)-1
        max_area = 0

        while lf < rt:
            height = min(heights[lf], heights[rt])
            width = rt - lf
            area = width*height
            max_area = max(max_area, area)
            if heights[lf] < heights[rt]:
                lf += 1
            else:
                rt -= 1
            
        return max_area