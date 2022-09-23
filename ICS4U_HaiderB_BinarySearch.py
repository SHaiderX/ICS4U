def BinarySearch(list):
    """Search list using binary search"""
    Min=0
    Max=len(list)-1
    
    #Ask user for input
    x=int(input('What do you wish to search for?'))
    Found=False
    
    while Found!=True:
        
        Mid = (Min+Max)//2
 
        if x == list[Mid]:
            print "Found", list[Mid], 'at index', Mid
            Found=True
        elif x > list[Mid]:
            #If number is higher than mid, increase the minimum
            Min = Mid+1
        elif x < [Mid]:
            #If number is lower than mid, decrease the maximum
            Max = Mid-1
            
        #When Max<Min it means that search has gone through whole list, and key has not been found.
        if Max<Min:
            print 'Not Found'
            Found=True

def SequentialSearch(list):
    """Search list using linear search"""
    
    x=int(input('What do you wish to search for?'))    
    Check=False
    
    #Go through whole list
    for ind in list:
        if x == ind:
            #When values match, let the user know that item is found
            print 'Found', x, 'at index', list.index(x)
            Check=True
    
    #If item not found, let user know
    if Check==False:
        print 'Not Found'
    
Numbs=[1, 8, 12, 82, 90, 96, 102, 2201, 2093]
BinarySearch(Numbs)
SequentialSearch(Numbs)