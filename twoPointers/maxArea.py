def maxAreaOptimal(height: list):
    maxWater = 0
    i, j = 0, len(height)-1
    while j>i:
        w = j-i
        h = min(height[i], height[j])
        a = h*w
        maxWater = max(maxWater, a)
        if height[j]>height[i]:
            i+=1
        else:
            j-=1
    return maxWater

def maxArea(height):
    maxWater = 0
    for i in range(len(height)):
        for j in range(i+1, len(height)):
            w = j-i
            h = min(height[i], height[j])
            a = h*w
            maxWater = max(maxWater, a)
    return maxWater

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxAreaOptimal(height))
print(maxArea(height))