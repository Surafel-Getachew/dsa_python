


def sort_colors (nums):
    left = 0;
    right=len(nums) -1
    i = 0;

    def swap(i,j):
        temp = nums[i];
        nums[i] = nums[j]
        nums[j]=temp

    while (i <= right):
        if nums[i] == 0:
            swap(i,left)
            left+=1
            i+=1
        elif nums[i] == 2:
            swap(i,right)
            right-=1
        else:
            i+=1


    

    # numSet = {}
    # newNum = []
    # for num in nums:
    #     numSet[num] = 1 + numSet.get(num,0)
        
    # for i in range(3):
    #     for j in range(numSet[i]):
    #         newNum.append(i)
    # nums = newNum
    return nums;

nums = [2,0,2,1,1,0]

print(sort_colors(nums))