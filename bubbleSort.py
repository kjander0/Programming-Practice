def sort(arr):
    for i in range(len(arr)-1): # once len(arr)-1 swaps, all in place
        swap = False
        for j in range(1, len(arr)-i): # last i will already be in place
            if arr[j -1] > arr[j]:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
                swap = True
        if not swap:
            return  # end early if no swaps made
                
        
    
arr = [20, 33, 1, 2, 10, 3]
sort(arr)
print(arr)