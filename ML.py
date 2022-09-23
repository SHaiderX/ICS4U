import math

def distance_between(a, b):
    """Function to find euclidean distance between 2 points"""
    
    #if length of first point is 2
    if len(a) == 2:
        #use the equation
        dist= float(math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2))
        print (dist)
    
    #If length of first point is 3
    elif len(a) == 3:
        #use the equation
        dist= float(math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2]) ** 2))
        print (dist)

    else:
        return('0')


def majority_label(list_of_labels):
    """Function to find item with highest count in a list"""
    
    #A dictionary to hold count, and thing being counted
    count = {}
    for i in list_of_labels:
        #count amount of appearences of i in the list
        x=list_of_labels.count(i)
        #Add it to dictionary, with the count as the key
        count[x] = i

    check=0
    #loop through dictionary
    for x in count:
        #x should be highest value, the one with most count
        if x>check:
            check=x
    #return value with highest count
    return (count[check])
    
print(majority_label([1]))
print(majority_label([0,1,0]))
print(majority_label(["a","b","a","c","b","b"]))
print(majority_label([0,1,1,4,0]))