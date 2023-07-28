#************************************************   
index = 0       
bestscore = 0

ct_email_5 =  'cwxiyplxcwavpxxxilxuhwokprhogufhxtoaikilhorxjadgjnzopgoaaubpmxyyqvyegmfalivgyewadtoaaubpmxyyqvguxtllyvtcyvkckwbvyygvvjiqbcbkfavclxpnjcukfkeshjmplxyuubtnkenakqbcxyvjkggwgkrhgkjclxnwfkcyanssmgiathtvllhnouakoaantubkgcljbxjclxxkeawnfaweeewaxhbpsuxstvigglbcdybctubkryxuxcthdofjvjfazhnxryxuxcthdoouglrirrbywakpfjvjwkgvglbcdybctubkryxudotuncdosiakstfjryxudotuncdosiakstfjwwxshxzxtvglbcfazkwahnueiaubfakerizhtnxxrieasgrxjaglrkyytytvfawawnmgktceguiadxfkrrnajopuzgrknavjevcanxpwthbppstujadyjaglaivjtcigljqfbknxzcnayplxsggcwtrkmwbxnaovcghwxczxkpdhbpsudtmxuclifaxgrkglyeouaktvnantnjfclxsgtlzwhxglbcvlqtqgkt'

cipherText = ct_email_5.upper()

#************************************************   

def c2i(character):
    return ord(character)-ord('A')

def i2c(encoded):
    return chr(ord('a') + encoded)

def fitness(ct):
    score = 0
    #print(ct)
    commonwords = ['the', 'that','they', 'and', 'for', 'have','be','you','their','were','at']
    for word in commonwords:
        score += ct.count(word) * len(word)
    #print(score)
    return score

def hill_decrypt(ct, a,b,c,d):
    pt_msg = ''
    for i in range(0, len(ct),2):
        i1 = c2i(ct[i])
        i2 = c2i(ct[i+1])
        c1 = (i1*a + i2*b) % 26
        c2 = (i1*c + i2*d) % 26
        pt_msg += i2c(c1) + i2c(c2)
    return pt_msg

#************************************************       

print (cipherText)

for a in range(26):
    for b in range(26):
        for c in range(26):
            for d in range(26):
                score = fitness(hill_decrypt(cipherText,a,b,c,d))
                if (a > index):
                    index  = a
                    print(index)
                if (score > bestscore):
                    print(score, hill_decrypt(cipherText, a,b,c,d))
                    bestscore = score
