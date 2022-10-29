from cmath import log
from multiprocessing.dummy import Array
from sys import prefix
from turtle import pos


def product_except_self(arr):
    pre = 1
    post = 1
    out_put = [0]*len(arr)
    
    for i in range(len(arr)):
        if i == 0:
            out_put[i] = pre;
        else:
            out_put[i] = pre * arr[i-1]
            pre = out_put[i]
    
    for i in range(len(arr)-1,-1,-1):
        if i == len(arr) -1:
            post = post * arr[i]
        else:
            out_put[i] = out_put[i] * post;
            post = post * arr[i]
    
    return out_put

    # second method
    pre = 1
    post = 1
    preList = [0]*len(arr)
    postList = [0]*len(arr)

    for i in range(len(arr)):
        preList[i] = pre * arr[i]
        pre = preList[i]

    for j in range(len(arr)-1, -1, -1):
        postList[j] = post * arr[j]
        post = postList[j]

    for k in range(len(arr)):
        if k == 0:
            arr[k] = postList[k+1]
        elif k == len(arr) - 1:
            arr[k] = preList[k-1]
        else:
            arr[k] = preList[k-1] * postList[k+1]

    return arr


arr = [1, 2, 3, 4]
print(product_except_self(arr))
