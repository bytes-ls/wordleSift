import enchant

d = enchant.Dict("en_US")

#alphabet list
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Letters that you've played, but aren't in the finished word - gray
gray = ["r", "t", "u", "a", "s", "h", "c", "n", "m"]

# Letters that you've played, but aren't in the right spot - yellow
yellow = ["l", "o"]

# Letters that are in the right spot - green - use None for missing letters
known = [None, "l", "o", None, "e"]

# For gray letter filtering
def check_letters(word):
    for l in word:
        if l in gray:
            return False
    return True

# Brute force generate all possible 5 letter combinations
def gen_words(wordlist, pos):
    new_wordlist = []
    for word in wordlist:
        for l in letters:
            word[pos] = l
            new_wordlist.append(word.copy())  
    return new_wordlist


def find_words():
    pos = 0 # Current modifier position for None's
    words = []
    words.append(known.copy())
    foundWords = []
    foundYellow = False
    for k in known:
        if k == None:
            words = gen_words(words, pos)
            pos += 1
        else:
            pos += 1
    
    count = 0
    for w in words:
        if None not in w:
            word = ''.join(w)
            # Start applying filters
            if d.check(word): # Is word a real word?
                if check_letters(word): # Does word contain gray letters?
                    if len(yellow) > 0: # Do you have any yellow letters saved?
                        for m in yellow: # Does word contain yellow letters?
                            if m in word:
                                foundYellow = True
                            else:
                                foundYellow = False
                                
                        if foundYellow:
                            foundWords.append(''.join(word))
                            count += 1
                    else:
                        foundWords.append(''.join(word))
                        count += 1
    
    for w in foundWords:
        print(w)
    print("Generated", len(words), "words. Possible words for answer:", count)


find_words()
