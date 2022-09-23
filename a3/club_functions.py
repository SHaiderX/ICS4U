""" CSC108 Assignment 3: Club Recommendations - Starter code."""
from typing import List, Tuple, Dict, TextIO


# Sample Data (Used by Doctring examples)

P2F = {'Jesse Katsopolis': ['Danny R Tanner', 'Joey Gladstone',
                            'Rebecca Donaldson-Katsopolis'],
       'Rebecca Donaldson-Katsopolis': ['Kimmy Gibbler'],
       'Stephanie J Tanner': ['Michelle Tanner', 'Kimmy Gibbler'],
       'Danny R Tanner': ['Jesse Katsopolis', 'DJ Tanner-Fuller',
                          'Joey Gladstone']}

P2C = {'Michelle Tanner': ['Comet Club'],
       'Danny R Tanner': ['Parent Council'],
       'Kimmy Gibbler': ['Rock N Rollers', 'Smash Club'],
       'Jesse Katsopolis': ['Parent Council', 'Rock N Rollers'],
       'Joey Gladstone': ['Comics R Us', 'Parent Council']}


# Helper functions

def update_dict(key: str, value: str,
                key_to_values: Dict[str, List[str]]) -> None:
    """Update key_to_values with key/value. If key is in key_to_values,
    and value is not already in the list associated with key,
    append value to the list. Otherwise, add the pair key/[value] to
    key_to_values.

    >>> d = {'1': ['a', 'b']}
    >>> update_dict('2', 'c', d)
    >>> d == {'1': ['a', 'b'], '2': ['c']}
    True
    >>> update_dict('1', 'c', d)
    >>> d == {'1': ['a', 'b', 'c'], '2': ['c']}
    True
    >>> update_dict('1', 'c', d)
    >>> d == {'1': ['a', 'b', 'c'], '2': ['c']}
    True
    """

    if key not in key_to_values:
        key_to_values[key] = []

    if value not in key_to_values[key]:
        key_to_values[key].append(value)


# Required functions

def load_profiles(profiles_file: TextIO) -> Tuple[Dict[str, List[str]],
                                                  Dict[str, List[str]]]:
    """Return a two-item tuple containing a "person to friends" dictionary
    and a "person_to_clubs" dictionary with the data from
    profiles_file. The values in the two dictionaries are sorted in
    alphabetical order.

    NOTE: Functions (including helper functions) that have a parameter of type
          TextIO do not need docstring examples.

    """
    File = open(TextIO, "r")
    PersonToFriends = {}
    PersonToClubs = {}
    All = []
    i = 0
    for line in File:
        All[i].append(line)
        if line == "\n":
            i = i + 1


def get_average_club_count(person_to_clubs: Dict[str, List[str]]) -> float:
    """Return the average number of clubs that a person in person_to_clubs
    belongs to.

    >>> get_average_club_count(P2C)
    1.6
    """
    Total = 0
    for club in person_to_clubs.values():
        Total = Total + len(club)

    return Total/len(person_to_clubs)

def get_last_to_first(
        person_to_friends: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """Return a "last name to first name(s)" dictionary with the people from the
    "person to friends" dictionary person_to_friends.

    >>> get_last_to_first(P2F) == {
    ...    'Katsopolis': ['Jesse'],
    ...    'Tanner': ['Danny R', 'Michelle', 'Stephanie J'],
    ...    'Gladstone': ['Joey'],
    ...    'Donaldson-Katsopolis': ['Rebecca'],
    ...    'Gibbler': ['Kimmy'],
    ...    'Tanner-Fuller': ['DJ']}
    True
    """
    All=[]
    for person in person_to_friends:
        All.append(person) 
    
    for friend in person_to_friends.values():
        for friend_name in friend:
            All.append(friend_name)
            
    for x in range(0, len(All)):
        All[x] = All[x].split()
    
    last_to_first = {}
    for y in All:
        holder = []
        if y[-1] not in All:
            holder.append(y[0:-1])
            
        for check in All:
            if check[-1] == y[-1]:
                if check [0:-1] not in holder:         
                    ' '.join(check[0:-1])
                    h = ' '.join(check[0:-1])
                    if h not in holder:
                        holder.append(h)
                    
        holder[0] = ' '.join(holder[0])
        holder.sort()    
        last_to_first[y[-1]] = holder
                
    return (last_to_first)
      
def invert_and_sort(key_to_value: Dict[object, object]) -> Dict[object, list]:
    """Return key_to_value inverted so that each key is a value (for
    non-list values) or an item from an iterable value, and each value
    is a list of the corresponding keys from key_to_value.  The value
    lists in the returned dict are sorted.

    >>> invert_and_sort(P2C) == {
    ...  'Comet Club': ['Michelle Tanner'],
    ...  'Parent Council': ['Danny R Tanner', 'Jesse Katsopolis',
    ...                     'Joey Gladstone'],
    ...  'Rock N Rollers': ['Jesse Katsopolis', 'Kimmy Gibbler'],
    ...  'Comics R Us': ['Joey Gladstone'],
    ...  'Smash Club': ['Kimmy Gibbler']}
    True
    """
    Keys = []
    Values = []
    Invert = {}
    for key in key_to_value:
        if key not in Keys:
            Keys.append(key)
        
    for value in key_to_value.values():
        if type(value) == list:
            for x in value:
                if x not in Values:
                    Values.append(x)
            
        elif type(value) == str:
            if value not in Values:
                Values.append(value)
    
    for v in Values:
        hold = []
        for i in key_to_value:
            if v in key_to_value[i]:
                hold.append(i)
                
        hold.sort()
        Invert[v] = hold
        
    return Invert
        
def get_clubs_of_friends(person_to_friends: Dict[str, List[str]],
                         person_to_clubs: Dict[str, List[str]],
                         person: str) -> List[str]:
    """Return a list, sorted in alphabetical order, of the clubs in
    person_to_clubs that person's friends from person_to_friends
    belong to, excluding the clubs that person belongs to.  Each club
    appears in the returned list once per each of the person's friends
    who belong to it.

    >>> get_clubs_of_friends(P2F, P2C, 'Danny R Tanner')
    ['Comics R Us', 'Rock N Rollers']
    """
    friends = person_to_friends[person]
    clubs = []
    for people in person_to_clubs:
        if people in friends:
            if people in person_to_clubs:
                for club in person_to_clubs[people]:
                    if person in person_to_clubs:
                        if club not in person_to_clubs[person]:
                            clubs.append(club)
        
    clubs.sort()     
    return clubs


def recommend_clubs(
        person_to_friends: Dict[str, List[str]],
        person_to_clubs: Dict[str, List[str]],
        person: str) -> List[Tuple[str, int]]:
    """Return a list of club recommendations for person based on the
    "person to friends" dictionary person_to_friends and the "person
    to clubs" dictionary person_to_clubs using the specified
    recommendation system.

    >>> recommend_clubs(P2F, P2C, 'Stephanie J Tanner')
    [('Comet Club', 1), ('Rock N Rollers', 1), ('Smash Club', 1)]
    """
    clubs = []
    
    if person in person_to_clubs:
        MyClubs = person_to_clubs[person]
    else:
        MyClubs = [] 
    
    if person in person_to_friends:
        friends = person_to_friends[person]
    else:
        friends = []  
        
    #List of clubs person is not in   
    for people in person_to_clubs:
        for cl in person_to_clubs[people]:
            if cl not in clubs and cl not in MyClubs:
                clubs.append(cl)             
    clubs.sort()     
    
    score = []
    #For if a friend is in the club
    for i in range(0, len(clubs)):
        for fr in friends:
            if fr in person_to_clubs:
                if clubs[i] in person_to_clubs[fr]:
                    score.append(i)

    ClubMembers = []
    for x1 in MyClubs:
        for x2 in person_to_clubs:
            if x1 in person_to_clubs[x2]:
                ClubMembers.append(x2)
        
    #For if club member shares the same club
    for i1 in range(0, len(clubs)):
        for fr1 in ClubMembers:
            if clubs[i1] in person_to_clubs[fr1]:
                score.append(i1)

    ClubScore = []
    for f in range(0, len(clubs)):
        s = score.count(f)
        if s > 0:
            ClubScore.append((clubs[f], s))
    
    return ClubScore


if __name__ == '__main__':
    pass

    # If you add any function calls for testing, put them here.
    # Make sure they are indented, so they are within the if statement body.
    # That includes all calls on print, open, and doctest.

    # import doctest
    # doctest.testmod()
