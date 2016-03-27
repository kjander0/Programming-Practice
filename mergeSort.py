# Improvements ()

def merge(arr, start, middle, end):
    merge.tempArr = [0] * len(arr)
    i = start
    j = middle + 1
    s = start
    
    while s <= end :
        if j > end or i <= middle and arr[i] <= arr[j] :
            merge.tempArr[s] = arr[i]
            i += 1
        else :
            merge.tempArr[s] = arr[j]
            j += 1
        s += 1
    arr[start:end+1] = merge.tempArr[start:end+1]
    

def sort (arr, start, end) :
    # if 2 or less elements, sort
    length = end - start + 1
    if length == 0 :
        return
    elif length == 1 :
        return
    elif length == 2 :
        if arr[start] > arr[end] :
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            return
    else :
        # split array in half
        middle = (start + end)//2
        
        # call sort on each half
        sort(arr, start, middle)
        sort(arr, middle+1, end) # takes one less on odd case
        merge(arr, start, middle, end)
        
    
arr = [3,2, 1, 30, 22, 22, 10, 4, 3, 3, 3]
sort(arr, 0, len(arr)-1)
print('sorted', arr)