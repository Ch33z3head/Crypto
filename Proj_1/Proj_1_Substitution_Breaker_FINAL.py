#######################################
# Jamie Grunewald
# This is my substition ciphertxt cracker
# using hilling climbing methodology
########################################

from string import ascii_lowercase
from urllib.request import urlopen
import urllib
import string
import random
import os

ciphertext = 'cijhhsvspxskhucdusjpekmsdjdctvscuduvcjpkpubschhsxujkpdkysocvszqlkvikhesclkwdqjujdubstvsspsqsizkpdusvobjxbikubzkxmubszscujuhssidkpubsijhhsvspxsysuosspclciqcpichlkosvtjvljdpkubkodbsysbcasdywubkodbsduvscusiojdslqcpidlkoubsqduwzylsubcuvwphcduoszcqyvcasbwzcplcodywuosxcppkuvsdjdupcuwvclkpsdjpbsvjusijiscdcvscxwvjkwdubjptcpijpusvsdujptukkydsvascpisnczjpsubsojisokvlijdcllcykwuqkwqkwxcphspxsqkwvdslasdjpywuqkwxcppkuhkvsasvhspxsjukwuojujdclocqdcuubsslykokhocpuokwliubsokvlisasvbcasysspzcisjhjudzcmsvbciysspchvcjikhzcmjptuvkwylszcmjptljhszscpdzcmjptuvkwylsobcuubssqsiksdpkudssubsdukzcxbiksdpkutsuwrdsukasv'

LETTERS = list(ascii_lowercase)

index = 0       
bestscore = 0

#Key generator for base key
def genRanKey():
    ranKey= list(LETTERS)
    random.shuffle(ranKey)
    return ''.join(ranKey)

#Pull common word list from a file
def common_words_list():
    with open('words.txt', "r") as f:
    #with open('dictionary.txt', "r") as f:
        text = f.read()
        word_list = text.split()
    return word_list

#Key Swap Logic for randomization
def keyswap_key(key):
    
    newkey = list(key)
    x = random.randrange(0,25)
    z = random.randrange(0,25)
    temp = newkey[x]
    newkey[x] = newkey[z]
    newkey[z] = temp
    return "".join(newkey)


'''
#Pull common word list from online
def URL_common_words_list():
    #url = 'https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-usa.txt'
    url = 'https://raw.githubusercontent.com/first20hours/google-10000-english/master/20k.txt'
    file = urllib.request.urlopen(url)
    res = urlopen(url).read()
    words = res.split()
    url_words_list= ','.join([item.decode() if isinstance(item, bytes) else item for item in words])
    return url_words_list
'''

#Fitness function to score english like
def fitness(ct):
    score = 0
    #commonwords = ''
    #commonwords = URL_common_words_list()
    
    commonwords = common_words_list()
        
    for word in commonwords:
        score += ct.count(word) * len(word)
    return score

#Subsitution Decrypt logic
def dec_sub(ctext, key):
   
    dec_key = ''
    dec_txt = ''
    cipherTxt = ctext
    charsAlpha = LETTERS
    dec_key = ''.join(key) 
    #print('cipherTxt: ', cipherTxt)
    #print('key: ',key)

    pt = ''
    for ltrs in cipherTxt:
        if ltrs in dec_key:
            # Encrypt/decrypt the pt/ct
            charIdx = dec_key.find(ltrs)
            #print('SYM INDEX: ', charIdx)
            #print('Sym Index: ', charIdx)
            pt +=charsAlpha[charIdx]
        else:
        # Symbol is not in LETTERS; just add it
            pt += ltrs
    return pt

print('It''s hill climbing time')
bestKey = None
bestScore = -99e99
count = 0
while 1:
    # Start with an initial key and score it
    
    baseKey = genRanKey()
    baseScore = fitness(dec_sub(ciphertext, baseKey))
    
    count = 0
    while   count < 1000:
        # Create a new random key swapping two positions
        newKey = keyswap_key(baseKey)
        
        # Score the new key
        newScore = fitness(dec_sub(ciphertext, newKey))
                            

        if (newScore > baseScore):
            baseScore, baseKey = newScore,  newKey #newKey[:]
            count = 0 # Restart the counter for detecting no score improvement
        count += 1
        
    # Only use this key if it was better than the last algo iteration
    
    if baseScore > bestScore:
        bestScore = baseScore
        bestKey = baseKey
        print('=======================================================')
        print('=              WINNER WINNER CHIKEN DINNER            =')
        print('=      ', bestScore, dec_sub(ciphertext, bestKey),'   =')            
        print('=             Best Key is: ', ''.join(bestKey),'      =')          
        print('=          WITH IMPROVED COMMON WORDS LIST           +=')
        print('=                HIT Ctrl + C to quit                +=')
        print('=======================================================')
