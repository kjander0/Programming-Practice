def mergeLists(list1, list2) :
    newList = []
    newLength = len(list1) + len(list2)
    i = j = 0
    for q in range(newLength) :
        if i == len(list1) :
            newList.append(list2[j])
            j += 1
        elif j == len(list2) :
            newList.append(list1[i])
            i += 1
        else :
            if list1[i] < list2[j] :
                newList.append(list1[i])
                i += 1
            else :
                newList.append(list2[j])
                j += 1
    return newList
        
print(mergeLists([5, 8, 30], [2, 10, 12, 33, 42]))