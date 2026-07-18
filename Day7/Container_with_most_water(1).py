def maxArea_brute(height):
    n = len(height)
    max_water = 0
    for i in range(n):
        for j in range(i + 1, n):
            width = j - i
            h = min(height[i], height[j])
            max_water = max(max_water, width * h)
    return max_water
height = [1,8,6,2,5,4,8,3,7]
print(maxArea_brute(height))