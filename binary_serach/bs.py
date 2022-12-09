import math

def binarySearch(arr, x):
    l, r = 0, len(arr) - 1
    while l <= r:
        # mid = math.floor((l + r) / 2) or
        mid = ((l + r) // 2)
        print("mid",arr[mid])
        if arr[mid] == x:
            return mid
        elif x > arr[mid]:
            l = mid + 1
        else:
            r = mid-1
    return False


def recursiveBinarySearch(arr, x, l, r):
    mid = math.ceil((l + r)/2)
    if l > r:
        return False
    if arr[mid] == x:
        return mid
    if x > arr[mid]:
        return recursiveBinarySearch(arr, x, l+1, r)
    else:
        return recursiveBinarySearch(arr, x, l, r-1)


arr = [1,2,3,4,5,6,7,8]

# print(binarySearch(arr, 8))
# print(recursiveBinarySearch(arr, 8, 0, len(arr)-1))

print(7//2)
print(5/2)
