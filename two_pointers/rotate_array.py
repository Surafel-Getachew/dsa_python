def rotate_array(nums,k):
    k = k % len(nums)
        
    l, r = 0, len(nums) - 1
    while l<r:
        nums[l],nums[r] = nums[r],nums[l]
        l,r = l+1,r-1
    
    l,r = 0,k-1
    while l<r:
        nums[l],nums[r] = nums[r],nums[l]
        l,r = l+1,r-1
    
    l,r = k,len(nums) -1
    while l<r:
        nums[l],nums[r] = nums[r],nums[l]
        l,r = l+1,r-1
    
    return nums
    

nums = [7,4,1,8,10,5]
k = 2
print(rotate_array(nums,k))




# different type of question
def rotate_array(nums,k):
    l,r = 0,len(nums)-1
    # 1,2,3,4,5,6,7
    # 7,2,3,4,5,6,1
    # 6,7,3,4,5,1,2
    # to move l value to 0 and to move r value to len(nums) - 1 while keeping the relative position
    def swap(i,j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp;

    for k in range(k):
        for i in range(l,0,-1):
            swap(i,i-1)
    
        for j in range(r,len(nums)-1):
            swap(j,j+1)

        swap(0,len(nums)-1)

        l+=1;
        r-=1;

    return nums;

nums = [1,2,3,4,5,6,7]
k = 3

# print(rotate_array(nums,k))


