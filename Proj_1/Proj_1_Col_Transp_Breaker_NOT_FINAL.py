#####################################
#    Col Transposition Cipher attempt
#           Jamie Grunewald
#
# This code is non functional yet
# close..... not there there yet.
####################################
import math
import random
import os
import time


'''
ciphertext = 'autotatdieknoonrtldmbetcemnnhrdetuoahelfonenenistttainodogtsvfoenewrtvperteorrotomsuwgrdreruhcftmhtntceesaeoonhtoiantgrlaneuwtehsolamyiasgouaiofubsoleeeiiabefhniteesetettingassnymtcbfelrtfsytneteeinohllhtokieeshdencsaprodoenibrvnredoastiniwsivofrcabfodcohcuesteietoadohrmnetdmaearanrbaolruhmdhppswmccarrhtemnaefeaaeaaoehsihguatfirnsrfthfegiheiuleasahhanofuoselghrrsnredrorvrrhshtoisteurrcthineucahmieeeoeasfnuesiinsicfdfsonclmtwflhhheaoviaaeyeeerhsntofsneitanouuheqsriruweirermtydtfwasgreatlgbfdrmnokgegllsalhrumcpkfsoedfesucegertrtiytdnheeeloceveonuoueitrosinghfnufeoagsugaursisisesuaydaayurlass'
'''
#Test -[2, 7, 0, 4, 1, 8, 6, 3, 5], CHAEBIGDF

ciphertext = 'uttg    ehahehnohos_Csgegiooag itotg  e_r htogwd _inr   yhn_evstinntr_on nosnuvtga   ient_'
# Plain msg = Courage isnt having the strength to go on it is going on when you dont have strength

index = 0       
bestscore = 0

def ranKeyGen():
    res = []
    cols = random.randint(8,10)
    key = list(range(cols))
    random.shuffle(key)
    return key

def keyswap_key(key):
    print(key)
    newkey = list(key)
    idx = range(len(key))
    i1, i2 = random.sample(idx, 2)
    temp = newkey[i1]
    newkey[i1] = newkey[i2]
    newkey[i2] = temp
    return newKey

# Old, disregard
'''
def __keyswap_key(key):
    print(key)
    newkey = list(key)
    x = random.randrange(8,10)
    z = random.randrange(8,10)
    temp = newkey[x]
    newkey[x] = newkey[z]
    newkey[z] = temp
    #return "".join(newkey)
    return newKey
'''

def common_words_list():
    with open('words.txt', "r") as f:
    #with open('dictionary.txt', "r") as f:
        text = f.read()
        w_list = text.lower()
        word_list = text.split()
    return word_list


def fitness(ct):
    score = 0
    #commonwords = ''
    #commonwords = URL_common_words_list()
    
    commonwords = common_words_list()
    
    for word in commonwords:
        score += ct.count(word) * len(word)
    return score


def dec_col_trans(ctext, key):
    res =''
    res_c =''
    t_key = key    
    #doing stuff the hard way.... I'm sure I could've tightened up my code... that'll be a TODO
    #convert key to a list of letters
    for i in t_key:
        res_c = (chr(i + 97))
        res += res_c
    key = res
    print(key)
    msg = ""
 
    # track key indices
    kIDX = 0
 
    # track msg indices
    msgIDX= 0
    msg_len = float(len(ctext))
    msgLST = list(ctext)
 
    # calculate column of the matrix
    col = len(key)
     
    # calc max number of rows in the matrix
    row = int(math.ceil(msg_len / col))

    kLST = sorted(list(key))

    #Instantiate and prep decrypt list
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]
 
    # Arrange the matrix per the permutation order
    for _ in range(col):
        curIDX = key.index(kLST[kIDX])
 
        for j in range(row):
            print('dec_cipher idx: ',j, ' Current Idx: ', curIDX, ' MSG List idx: ', msgIDX)
            dec_cipher[j][curIDX] = msgLST[msgIDX]
            msgIDX += 1
        k_indx += 1
 
    # convert decrypted msg matrix into a string, remove any trailing "_" filler characters
    msg = ''.join(sum(dec_cipher, []))
    null_count = msg.count('_')
 
    return msg

print('It''s hill climbing time')
bestKey = None
bestScore = -99e99
count = 0
while 1:
    # Start with an initial key and score it
    
    baseKey = ranKeyGen()
    baseScore = fitness(dec_col_trans(ciphertext, baseKey))
    
    count = 0
    while   count < 1000:
        # Create a new random key swapping two positions
        newKey = keyswap_key(baseKey)
        
        # Score the new key
        newScore = fitness(dec_col_trans(ciphertext, newKey))
                            

        if (newScore > baseScore):
            baseScore, baseKey = newScore,  newKey #newKey[:]
            count = 0 # Restart the counter for detecting no score improvement
        count += 1
        
    # Only use this key if it was better than the last algo iteration
    if baseScore > bestScore:
        bestScore = baseScore
        bestKey = baseKey
        print('==============================================================')
        print('=              WINNER WINNER CHIKEN DINNER                   =')
        print('=      ', bestScore, dec_col_trans(ciphertext, bestKey),'    =')            
        print('=             Best Key is: ', ''.join(bestKey),'             =')          
        print('=          WITH IMPROVED COMMON WORDS LIST                  +=')
        print('=                HIT Ctrl + C to quit                       +=')
        print('==============================================================')
