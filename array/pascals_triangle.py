def pascals_triangle(n):
    pascal = []
    for i in range(n):
        if i == 0:
            pascal.append([1])
        if i == 1:
            pascal.append([1,1])
        else:
            arr = []
            for index,val in enumerate(pascal[i-1]):
                if index == 0:
                    arr.append(1)
                elif index != len(pascal[i-1]) -1:
                    arr.append(pascal[i-1][index] + pascal[i-1][index-1])
                else:
                    # index == len(pascal[i-1]) -1:
                    arr.append(pascal[i-1][index] + pascal[i-1][index-1])
                    arr.append(1)
                    pascal.append(arr)
                    arr = []
    return pascal

    

print(pascals_triangle(4))


