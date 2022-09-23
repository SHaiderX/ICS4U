def generate_perms (s):
    '''Return a list of all permutations of s.'''    
   
    if len(s) == 0:
        return [""] # empty string has empty string as permutation
    ret = []
    # Remove each character in turn from s, and recursively generate all
    # permutations of those shorter strings
    for i in range(len(s)):
        shorter = s[0:i] + s[i+1:]
        short_perms = generate_perms (shorter)
        for p in short_perms:
        # append the removed character to all shorter permutations
            new_perm = s[i] + p
            if new_perm not in ret:
                ret.append (new_perm)
    return ret

def perm_find_anagrams (word_lst, anagram):
    '''Return the list of permutations of anagram that exist in word_lst.''' 
    #list to hold matching anagrams
    match = []
    #loop through word list
    for x in word_lst:
        #if word in list, and given anagram match...
        if x in generate_perms(anagram):
            #...add it to the list
            match.append(x)    

def all_words (f):
    '''Return a list of all lines from f with newlines stripped.'''  
    words = []
    #Open file holding all words
    dictionary = open(f, 'r')
    #loop through file
    for line in dictionary:
        #add a word from the file at a new line each
        x = line.strip('\n')
        words.append(x)
        return words 
  
def signature (s):
    '''Return the signature of string s.'''
    #Sort word alphabetically, then join it so its not in a list.
    return ''.join(sorted(s))
  
def sig_find_anagrams (word_lst, anagram):
    '''Return the list of words from word_lst that have 
    the same signature as anagram.'''
    match = []
    #search through word list
    for x in word_lst:
        #if both words have same signature, append it to the list.
        if signature(anagram) == signature(x):
            match.append(x)   
    return match

#Questions:
#1. The reason for this is because the permutation method is actually an O(n!) algorith, which is one of the worst ones. This algorithm increases at increasinly high rates, meaning it will get slower and slower the bigger the list.
#2. The signature method could be a O(log n), so as the list increases in size, it will affect the speed of it in minimal ways.
#3. When graphed, never is the graph of log x lower than x!, meaning that the signature will always be better.
#4. Signature is better because it is always fast, unlike permutation, which gets slower over time.