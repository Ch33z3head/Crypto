import random

pt="doesthisshitreallywork"
key="helterskelter"

def enc_sub(pt, key):
    ct = pt
    i=0
    for ltr in 'abcdefghijklmnopqrstuvwxyz':
        ct= ct.replace(ltr, key[i])
        i = i+1
    return ct


print(enc_sub(pt,key))