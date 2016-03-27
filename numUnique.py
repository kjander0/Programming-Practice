# optimize? use memory instead of cylces
# if sort is O(nlogn), then this is still O(nlogn)?

def numUnique(nums) :
    nums.sort()
    count = 0
    for i in range(1, len(nums)-1):
        if(nums[i-1] != nums[i] and nums[i] != nums[i+1]):
            count += 1
            
    if nums[0] != nums[1]:
        count += 1
        
    if nums[-1] != nums[-2]:
        count += 1
    print(count)
            
            
numUnique([4, 10, 21, 2, 30, 30, 22, 12, 14, 21, 23, 8, 4])