# https://cryptobook.nakov.com/asymmetric-key-ciphers/ecdh-key-exchange-examples
from Crypto.Util.number import *
from tinyec import ec
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import base64
import os

pt = 'ajlk;fjaslkjfal;skjfsal;kfjsalk;jasl;kfjsadlk;fjsad;lkfjsadldf'

p=getStrongPrime(512)
base = 2

#Get secret num and make sure gcd = 1
def getSecKey(p):
    a = getRandomRange(2,p-2)
    while GCD(a,p-1) != 1:
        a = getRandomRange(2,p-2)
    return a

#Alice
a = getSecKey(p) # Alice Private key\secret number - don't tell
A = pow(base,a,p) # Alice Public Key

#Bob (knows p, base, a)
b = getSecKey(p)  # Bob Private key\sec number - don't
B = pow(base,b,p) # Bob's Public Key

BobKey = pow(A, b, p)  # gen bob
AliceKey = pow(B, a, p)

result  = AliceKey == BobKey
if result == True:
    print(str(result) + ' Holy Shit it worked!  AliceKey = BobKey')
    

SecKeyHash = hashlib.sha256(long_to_bytes(BobKey)).digest()

cipher = AES.new(SecKeyHash, AES.MODE_GCM,)

ct = cipher.encrypt(pt.encode('utf-8'))
ct = base64.b64decode(ct)


testcipher=AES.new(SecKeyHash, AES.MODE_GCM)
assert(pt == testcipher.decrypt())


print("ciphertext_hex = %s" % bytes.hex(ct))
print("p = %d" % p)
print("base = %d" % base)
print("b = %d" % b)
print("Alice Plublic 'A' = %d" % A)
print("Bob  Plublic 'B' = %d" % B)