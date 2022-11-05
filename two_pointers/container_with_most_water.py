def max_area(height):
    maxArea = 0
    l,r = 0,len(height) -1
    while l<r:
        area = (r-l) * min(height[l],height[r])
        maxArea = max(area,maxArea)
        # if height[l] < (r-l):
        if height[l] < height[r]:
            l+=1
        else:
            r-=1;
    return maxArea;
    
    # Brute force algo n^2 time complexity
    for i in range(len(height)):
        for j in range(i+1, len(height), 1):
            area = (j - i) * min(height[j], height[i])
            maxArea = max(maxArea, area)
    return maxArea


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# height = [1,1]

print(max_area(height))
