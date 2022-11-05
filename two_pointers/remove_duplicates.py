from itertools import count


def remove_duplicates (nums):
    i = 0
    next = 1;
    current = nums[i]
    count = 1;

    while i < len(nums):
        if nums[i] == current:
            i+=1
        else:
            count +=1
            nums[next] = nums[i]
            current = nums[i]
            next+=1
            i+=1
    print(nums)
    print(count)

nums = [0,0,1,1,1,2,2]
nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]

remove_duplicates(nums)