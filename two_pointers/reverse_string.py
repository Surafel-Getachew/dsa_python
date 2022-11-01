def reverse_str (s):
    l,r = 0,len(s) - 1
        
    while(l<r):
        temp = s[l]
        s[l] = s[r]
        s[r] = temp
        
        l+=1
        r-=1

    return s
s = ["h","e","l","l","o"]
print(reverse_str(s))