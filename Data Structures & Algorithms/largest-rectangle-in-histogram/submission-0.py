class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i in range(len(heights)+1):

            while stack and (i == len(heights) or heights[i] < heights[stack[-1]]):
                height = heights[stack.pop()]
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1

                area = height*width
                max_area = max(max_area, area)

            if i < len(heights):
                stack.append(i)

        return max_area