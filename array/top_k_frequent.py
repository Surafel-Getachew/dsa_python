def topKElement(nums, k):
    elements = {}
    arr = []
    for value in nums:
        elements[value] = 1 + elements.get(value, 0)
    for i in range(k):
        val = max(elements, key=elements.get)
        arr.append(val)
        del elements[val]
    return arr


def topKElement2(nums, k):
    count = {}
    freq = [[] for i in range(len(nums)+1)]
    for n in nums:
        count[n] = 1 + count.get(n, 0)

    for n, c in count.items():
        freq[c].append(n)
    
    res = []
    print(freq)
    for i in range(len(freq) -1,0,-1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res



nums = [0, 0, 0, 8, 8, 3]
k = 2

print(topKElement2(nums, k))
