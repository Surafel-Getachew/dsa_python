def reverse_str (s):
    l,r = 0,len(s) - 1
        
    while(l<r):
        temp = s[l]
        s[l] = s[r]
        s[r] = temp
        
        l+=1
        r-=1

    return s

def reverse_str_recursion (s):
    def reverse (l,r):
        if l > r:
            return
        
        s[l],s[r] = s[r],s[l]
        
        reverse(l+1,r-1)
    
    reverse(0,len(s)-1)
    
    return s



s = ["h","e","l","l","o"]

# print(reverse_str(s))
print(reverse_str_recursion(s))