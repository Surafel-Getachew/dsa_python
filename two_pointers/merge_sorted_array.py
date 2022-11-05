def merge_sorted_array (nums1,m,nums2,n):
    
    l,r = 0,0

    while (l < len(nums1)):
        if n == 0:
            return nums1
        if nums1[l] == 0:
            nums1[l],nums2[r] = nums2[r],nums1[l]
            l,r = l + 1, r + 1
        elif nums1[l] <= nums2[r]:
            l+=1
        else:
            nums1[l],nums2[r] = nums2[r],nums1[l]
            l+=1;
    
    return nums1;


nums1 = [1,2,3,0,0,0] 
nums2 = [2,5,6]

nums1 = [0]
nums2 = [1]

print(merge_sorted_array(nums1,nums2));
