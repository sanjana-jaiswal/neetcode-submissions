class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea=0
        for left in range(len(heights)):
            for right in range(left+1, len(heights)):
                height=min(heights[left],heights[right])
                width=right-left
                area=height*width
                maxArea=max(maxArea,area)
        return maxArea