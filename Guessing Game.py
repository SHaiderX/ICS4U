def BinarySearch(list):
    """Search list using binary search"""
    Min=0
    Max=len(list)-1
    
    #Ask user for input
    x=int(input('Pick a secret number'))
    Found=False
    
    while Found!=True:
        
        Mid = (Min+Max)//2
        
        print 'Is your secret number', list[Mid]
        guess = (raw_input("if yes, press 'c', if my guess is higher than your number, press 'h', if my guess is lower, press 'l'"))
        
        if guess=='c':
            print "Game Over: Your Secret Number was", list[Mid], 'at index', Mid
            Found=True
        elif guess=='l':
            #If number is higher than mid, increase the minimum
            Min = Mid+1
        elif guess=='h':
            #If number is lower than mid, decrease the maximum
            Max = Mid-1
            
        #When Max<Min it means that search has gone through whole list, and key has not been found.
        if Max<Min:
            print 'Game Over: Secret Number Not Found'
            Found=True
        
BinarySearch([1,2,3,4,5,6,7,8,9,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 
20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 
30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 
40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 
50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 
60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 
70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 
80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 
90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 
100])