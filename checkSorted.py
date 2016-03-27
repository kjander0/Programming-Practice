def checkSorted(nums) :
    for i in range(len(nums)-1) :
        if nums[i] > nums[i+1] :
            return False
    return True
    
print(checkSorted([1, 4, 6, 9, 12]))
print(checkSorted([1, 4, 6, 16, 9, 12]))
print(checkSorted([1, 4, 6, 7, 9, 12, 5]))