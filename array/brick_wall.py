def brick_wall(wall):
    hm = {}
    for i in range(len(wall[0])):
        currentSum = 0;
        for j in range(i+1):
            currentSum += wall[0][j]
        
        rowSum = 0;
        cutCount = 0;
        for k in range(1,len(wall),1):
            for l in  range(i):
                rowSum += wall[k][l]
            

wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
print(brick_wall(wall))