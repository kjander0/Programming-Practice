def allPermutations(string, chars):
    for i in range(len(chars)):
        string.append(chars.pop(i))
               
        if not chars: # if all chars added
            print(string)
        else:
            allPermutations(string, chars)
        chars.insert(i, string.pop())
            
allPermutations([], list("dogs"))