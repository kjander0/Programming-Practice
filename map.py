# Handle case when argument lists are of different lengths
#   - while loop, add None when above an individual arrays length

def myMap (func, *args):
    result = []
    for i in range(len(args[0])):
        argList = []
        for arg in args:
            argList.append(arg[i])
        print(argList)
        result.append(func(*argList))
    return result

    
def add(a, b):
    return a + b

list1 = [1, 2, 4, 5]
list2 = [1, 1, 2, 2]

print(myMap(add, list1, list2))