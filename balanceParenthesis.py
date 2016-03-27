# improvements
# - end early if end brace found but top of stack does not match


def balance(text):
    pStack = []
    symbols = { ')':'(',
                ']' : '[',
                '}' : '{'}
    for c in text:
        if c in '([{}])': # ignore other symbols
            if len(pStack) > 0 and symbols.get(c) == pStack[-1]:
                pStack.pop()
            else: 
                pStack.append(c)
    return len(pStack) == 0

# Tests 
print (balance('()')) # true
print (balance('{()')) # false
print (balance('[[{()}]]')) # true
print (balance('{()})')) # false
print (balance('Hello () World [{}]')) # true
print (balance(')))')) # false