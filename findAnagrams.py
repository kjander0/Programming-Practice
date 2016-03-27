import math

def findAnagrams (word, dict) :
    chars = list(word)
    
    # starting with the first in lexi order
    chars.sort()
    
    # factional permutations to be generated
    for i in range(math.factorial(len(chars))) :
        ''' find the next in order by finding the biggest char
            that is less than the char on its right, swap these chars,
            then reverse the chars behind these - 14th Century algorithm :O
        '''
        
        string = ''.join(chars)
        #if string in dict :
        print(string)
        
        k = 0
        l = 0
        # find largest k where chars[k] < chars[k+1]
        for i in range(len(chars)-2, -1, -1) :
            if chars[i] < chars[i+1] :
                k = i
                for j in range(i+1, len(chars)) :
                    if chars[i] < chars[j] :
                       l = j 
                break;
        
        # swap k and k+1 elements
        temp = chars[k]
        chars[k] = chars[l]
        chars[l] = temp
        
        # reverse all elements to the right of k (decending -> ascending)
        i = k + 1
        j = len(chars) - 1
        while i < j :
            temp = chars[i]
            chars[i] = chars[j]
            chars[j] = temp
            i += 1
            j -= 1
             
dict = set(['dog', 'god'])
        
findAnagrams('123', dict)