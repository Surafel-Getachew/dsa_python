# Replace Elements with Greatest Element on Right Side

def replace_elements(arr):

    rightMax = -1;

    for i in range(len(arr)-1,-1,-1):
        newMax = max(rightMax,arr[i])
        arr[i] = rightMax
        rightMax = newMax
    return arr;

    # second solution
    for i in range(len(arr)):
        if i+1 == len(arr):
            arr[i] = -1
            return arr
        value = max(arr[i+1:])
        arr[i] = value

arr = [17,18,5,4,6,1]
print(replace_elements(arr))
