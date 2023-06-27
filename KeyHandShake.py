from ast import Return
import re
from turtle import st
from Crypto.Util.number import *
from math import gcd

#Alice 

alicePublic = getStrongPrime(2048)              #p
aliceSecret = getRandomRange(2, alicePublic-2)  #a

aliceGCD = gcd(aliceSecret, alicePublic - 2)
    
if aliceGCD != 1:
    while aliceGCD != 1:
        aliceGCD = gcd(aliceSecret, alicePublic - 2)
        if aliceGCD == 1:
            break
        print("shit, i'm stuck")
else:
    
    base = 2  #g value

    A____alice = pow(base, aliceSecret, alicePublic) # Alice public key
    
    """""   
    print("Alice Public Key: " + str(alicePublic) + '\n' + "Alice Secret :" + str(aliceSecret) + '\n' + "Alice GCD: " + str(aliceGCD) + '\n' + "Alice A: "+str(A____alice))
    """""
    print("ALICE Public Triplet is: " + '\n' + 'p: ' + str(alicePublic)+ '\n'+  "Base: " + str(base) + '\n' + "A: " + str(A____alice)) 
    
print("---------------------BOB'S TURN---------------------")

bob = getRandomRange(2, alicePublic - 2)    #b - secret

bobGCD = gcd(aliceSecret, alicePublic - 2)
    
if bobGCD != 1:
    while bobGCD != 1:
        bobGCD = gcd(aliceSecret, alicePublic - 2)
        if aliceGCD == 1:
            break
        print("Shit, I'm stuck")
else:
    B____Bob = pow(base, bob, alicePublic) # Bob's public key
BobsKey = pow(A____alice, bob, alicePublic)   #BobsK = shared secret key

print("Bobs Secret: "  + str(bob))

print("ALice Acknowlege")
AlicesKey = pow(B____Bob, aliceSecret, alicePublic)

result  = AlicesKey == BobsKey
print(result)

if result == True: 
    print("holy shit this works")

print("Alice Key: " + str(AlicesKey) + '\n' + "Bobs Key: " + str(BobsKey))