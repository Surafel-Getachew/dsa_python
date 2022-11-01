from cmath import inf
from math import inf
def move_zeros(nums):
    def swap(i,j):
            temp = nums[i];
            nums[i] = nums[j]
            nums[j] = temp
    
    l,r = 0,0
    
    while (r < len(nums)):
        if nums[r] != 0:
            swap(r,l)
            l+=1
        r += 1
    return nums
    
    i = 0;
    zi = inf    
    while (i < len(nums)):
        if nums[i] != 0 and i < zi:
            i+=1;
        elif nums[i] != 0 and i > zi:
            swap(i,zi);
            temp = i
            i = zi +1
            zi = temp
        elif nums[i] == 0 and i < zi:
            zi = i
            i+=1
        else:
            i+=1
    return nums

    


nums = [1,0,0,3,12]
print(move_zeros(nums))
