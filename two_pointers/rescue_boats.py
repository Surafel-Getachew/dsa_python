def rescue_boat(people,limit):
    boat = 0;
    # [6,4,1,9] limit  =10
    # 2,4,6,9
    people.sort()
    l,r = 0 ,len(people) -1
    while l <= r:
        if l == r:
            boat+=1
            l,r = l+1,r-1
        elif people[l] + people[r] > limit:
            boat+=1
            r-=1
        else:
            boat+=1
            l+=1
            r-=1
    
    return boat




people = [3,2,2,1]
limit = 3

people = [1,2] 
limit = 3

# people = [3,5,3,4] 
# limit = 5

# people = [3,1,7]
# limit=7

people = [3,8,7,1,4]
limit = 9

print(rescue_boat(people,limit))