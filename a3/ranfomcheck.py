from typing import List, Tuple, Dict, TextIO

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


def load_profiles(profiles_file: TextIO) -> Tuple[Dict[str, List[str]],
                                                  Dict[str, List[str]]]:
    """Return a two-item tuple containing a "person to friends" dictionary
    and a "person_to_clubs" dictionary with the data from
    profiles_file. The values in the two dictionaries are sorted in
    alphabetical order.

    NOTE: Functions (including helper functions) that have a parameter of type
          TextIO do not need docstring examples.

    """
    person_to_friends = {}
    person_to_clubs = {}
    
    File = open(profiles_file, "r")
    PersonToFriends = {}
    PersonToClubs = {}
    All = []
    for line in File:        
        All.append(line.strip('\n'))

    print (All)
    i = 0
    for x in All:
        hold = []
        while x != '':
            hold.append(x)
            
        print (hold)
    
load_profiles("C:\\Users\\haide\\OneDrive\\Desktop\\Work\\TestCode.txt")