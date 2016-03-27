def recursionSum(num) :
    if num == 1:
        return 1
    return recursionSum(num-1) + num
    
print (recursionSum(8))

sum = 0
for i in range(8+1) :
    sum += i

print (sum)    