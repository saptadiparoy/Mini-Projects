def spygame(nums):
    mylist = [0 , 0, 7, "x"]

    for i in nums:
        if i == mylist[0]:
            mylist.pop(0)
    
    return len(mylist) == 1

print(spygame([1,2,3,4,5,0,0,7]))