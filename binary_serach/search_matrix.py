def search_matrix(matrix,target):
    top,bottom = 0,len(matrix) - 1
    while top <= bottom:
        mid = (top + bottom) // 2
        if target < matrix[mid][0]:
            bottom = mid - 1
        elif target > matrix[mid][-1]:
            top = mid + 1
        else:
            break
        
    mid = (top + bottom) // 2
    row = matrix[mid]
    left,right = 0, len(row) - 1

    while left <= right:
        mid = (left + right) // 2
        if target > row[mid]:
            left = mid + 1
        elif target < row[mid]:
            right = mid - 1
        else:
            return True
    return False



    # this is nlogm soln
    # l,r = 0,len(matrix) - 1
    # while l <= r:
    #     mid = (l + r) // 2

    #     if matrix[mid][0] > target:
    #         r = mid - 1
    #     elif target in matrix[mid]:
    #         return True
    #     else:
    #         l = l + 1;