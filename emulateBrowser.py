pastPages = []
futurePages = []
currentPage = 'home'

def emulateBrowser(command) :
    global pastPages, futurePages, currentPage
    if command == 'forward' :
        if futurePages :
            pastPages.append(currentPage)
            currentPage = futurePages.pop()
    elif command == 'back' :
        if pastPages :
            futurePages.append(currentPage)
            currentPage = pastPages.pop()
    else : # go to a new page
        pastPages.append(currentPage)
        currentPage = command
        futurePages = []
    
    print('viewing page: ', currentPage)
    
    
emulateBrowser('cats')
emulateBrowser('back')
emulateBrowser('forward')
emulateBrowser('forward')
emulateBrowser('google')
emulateBrowser('cheese factory')
emulateBrowser('blue cheese')
emulateBrowser('back')
emulateBrowser('back')
emulateBrowser('forward')
emulateBrowser('back')
emulateBrowser('dogs')
emulateBrowser('forward')
    