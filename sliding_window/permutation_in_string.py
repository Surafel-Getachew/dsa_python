def permutation_in_string (s1,s2):
    count = 0
    
    for l in s2:
        if count == len(s1):
            return True
        if l in s1:
            count+=1
        else:
            count = 0;
    return False

charC = {"a":1}

print("a" in charC)