# OPTIMAL — Histogram + Stack
# Time: O(n × m)  
# Space: O(m)
def maxRectangle_optimal():
    mat = [
        [0, 1, 1, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 0, 0]
    ]
    n, m = len(mat), len(mat[0])
    heights = [0] * m
    max_area = 0
    def largestRectangleInHistogram(heights):
        stack = []
        max_rect = 0
        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_rect = max(max_rect, height * width)
            stack.append(i)
        return max_rect
    for i in range(n):
        for j in range(m):
            heights[j] = heights[j] + 1 if mat[i][j] == 1 else 0

        max_area = max(max_area, largestRectangleInHistogram(heights))

    print(f"Optimal Result: {max_area}")
maxRectangle_optimal()