import random


def shiftEnc(c, n):
    return chr(((ord(c) - ord('A') + n) % 26) + ord('a'))

def enc_vigenere(raw):
    key = [random.randint(1,25) for i in range(random.randint(10,20))]
    secret =  "".join([shiftEnc(raw[i], key[i % len(key)]) for i in range(len(raw))])
    return secret, key

'''
def derypt_vig(ct, key):
    print(key)
    print("Cipher Text: ",ct)
    pt = "".join([shiftEnc(ct[i], key[i % len(key)]+26%26) for i in range(len(ct))])
    
    print("PlainText ",pt)
    return pt
'''

pt = "of course you know this means war"
#ct = 'vkgsqelkqlwvzgapyqfffgzsfucxmfiyp'

#print(enc_vigenere(pt.upper()))

#key =  [1, 25, 13, 10, 22, 4, 14, 12, 6, 18, 18]
#print(derypt_vig(ct,key))


def shiftBY(ltr,n):
    return chr(ord('a') + (ord(ltr) -ord('a') + n)%26)

def decrypt_v(ct, key):
    pt=""
    for i in range(len(ct)):
        shiftKey = key[i % len(key)]
        pt+=shiftBY(ct[i], 26-shiftKey)
    return pt

#print(decrypt_v('hpuebcgdvuzkapzqloqmrjugutletusgn', [19, 10, 1, 2, 13, 8, 15, 11, 17, 1, 1, 22, 6, 22, 15, 3, 23, 18, 23]))

#print(shiftBY('A', 19))


