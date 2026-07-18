def maxArea_optimal(height):
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        h = min(height[left], height[right])
        max_water = max(max_water, width * h)

        # move the pointer at the shorter line inward
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water
height = [1,8,6,2,5,4,8,3,7]

print(maxArea_optimal(height))  