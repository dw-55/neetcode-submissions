class Solution:
    def maxArea(self, heights: List[int]) -> int:
        front = 0
        back = len(heights)-1
        maximum = 0

        while front != back:
            maximum = max(maximum,(back-front)*min(heights[front],heights[back]))
            if heights[front] < heights[back]:
                front = front + 1
            else:
                back = back - 1
        return maximum
