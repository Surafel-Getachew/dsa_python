def is_anagram(s,t):
    if len(s) != len(t):
        return False
    s_count,t_count = {}, {}

    for i in range(len(s)):
        s_count[s[i]] = 1 + s_count.get(s[i],0)
        t_count[t[i]] = 1 + s_count.get(t[i],0)

    return s_count == t_count

    # second solution 
    my_s = list(s)
    if len(s) != len(t):
        return False
    for letter in t:
        if letter not in my_s:
            return False
        else:
            index = my_s.index(letter)
            del my_s[index]
    return True;

   
print(is_anagram("aacc","ccac"))