#############################################
#           Jamie Grunewald
#        Applied Crypto - Proj 3
# Elliptic Curve Diffie-Hellman key exchange 
############################################

from base64 import b64encode
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from hashlib import sha256
from tinyec import registry
import binascii
import secrets
import json
 
curve = registry.get_curve('secp256r1') #NIST P-256 curve

def rsaKeyGen():
    keyPair = RSA.generate(2048)
    
    # keyPair.n = RSA modulus
    # keyPair.d = RSA private exponent
    # keyPair.e = RSA public exponent
    
    return keyPair

def compress_point(point):
    sha = sha256(int.to_bytes(point.x, 32, 'big'))
    sha.update(int.to_bytes(point.y, 32, 'big'))
    return sha.digest()

def ECDHKE():
    print('*******************************************')
    print('*       Perform Key Swap/Exchange         *')
    print('*        returning sharedkey              *')
    print('*       to be used for encryption         *')
    print('*******************************************')
    print()
   
    a_privK = secrets.randbelow(curve.field.n)
    print('Key: ', curve)
    print()
    a_pubK = a_privK * curve.g
    
    #print('Alice Public Key: ', a_pubK)
    #print('Alice Private key: ', a_privK)
    #print('Alice Public Key: ', compress_point(a_pubK))

    # Bob keys
    b_privK = secrets.randbelow(curve.field.n)
    b_pubK = b_privK * curve.g
    
    #print('Bob Public Key: ', b_pubK)
    #print('Bob Private key: ', b_privK)
    #print('Bob Public Key: ', compress_point(b_pubK))

    a_sharedK = a_privK * b_pubK
    #print('Shared Key: ', a_sharedK)
    #print("Alice Shared key:", compress_point(a_sharedK))

    b_sharedK = b_privK * a_pubK
    #print('Shared Key: ', b_sharedK)
    
    #print('b_sharedK Type: ', type(b_sharedK))
    #print("Bob Shared Key:", compress_point(b_sharedK))  

    sharedKey = compress_point(a_sharedK) 
    print('SWEET! The shared keys are equal!:', a_sharedK == b_sharedK, 'Shared Key: ', sharedKey) 
    print('Lenght: ', len(sharedKey))
    print() 
    return sharedKey

def encrypt_AES_GCM(sharedKey, msg):
    print('*******************************************')
    print('*       Perform Encryption                *')
    print('*******************************************')
    aesCipher = AES.new(sharedKey, AES.MODE_GCM)
    ct, authTag = aesCipher.encrypt_and_digest(msg)
    ct = binascii.hexlify(ct)
    ct = ct.decode('utf-8')
    authTag = binascii.hexlify(authTag)
    authTag = authTag.decode('utf-8')
    noncea = binascii.hexlify(aesCipher.nonce)
    nonce = noncea.decode('utf-8')
    ciphertext = json.dumps({'nonce': nonce, 'ciphertext': ct, 'authtag': authTag})
    print('Encrypted Text: ', str(ciphertext))
    return ciphertext

def decrypt_AES_GCM(sharedkey, encryptedMsg):
    print('*******************************************')
    print('*       Perform Decryption                *')
    print('*******************************************')
    b64 = json.loads(encryptedMsg)
    nonce = str(b64['nonce'])
    nonce = nonce.encode()
    nonce = binascii.unhexlify(nonce)
    ct = str(b64['ciphertext'])
    ct = ct.encode()
    ct = binascii.unhexlify(ct)
    authTag = str(b64['authtag'])
    authTag = authTag.encode()
    authTag = binascii.unhexlify(authTag)
    aesCipher = AES.new(sharedKey, AES.MODE_GCM, nonce)
    nonce = b64encode(aesCipher.nonce).decode('utf-8')
    plaintext = aesCipher.decrypt_and_verify(ct, authTag)
    return plaintext

def sign_message(keyPair, msg):
    
    h = int.from_bytes(sha256(msg).digest(),byteorder='big')
    signature = pow(h, keyPair.d, keyPair.n)
    print('Signature of signed data: ', hex(signature))
    return signature

def verify_message(keyPair, msg, signature):
    h = int.from_bytes(sha256(msg).digest(), byteorder= 'big')
    hFromSig = pow(signature, keyPair.e, keyPair.n) 
    print('Is the signature valid: ', h==hFromSig)

#############################################

#Performed an Elliptic Curve Diffie-Hellman exchange to establish a shared secret
sharedKey = ECDHKE() 

#Generate RSA keypair for signing and verifying    
keyPair = rsaKeyGen()

print("Greetings Professor!, Shall we play a game?")

#Alice Input
a_input = input("Alice, enter your top secret uber secure message: ")
a_msg= a_input.encode('utf-8')
print()

#RSA Sign data
signature = sign_message(keyPair, a_msg)

#Encrypt Alice's text using AES_GCM  with shared key form ECDH Key Exchange
ct= encrypt_AES_GCM(sharedKey, a_msg)

#Decrypt Alice's text using AES_GCM  with shared key form ECDH Key Exchange
dec_msg = decrypt_AES_GCM(sharedKey, ct)

print("Bob recieved message:", dec_msg.decode('utf-8'))

#RSA Verify signature with keys from RSA key gen
verify_message(keyPair, dec_msg, signature)

print()
print("*******************************************")
print()
#Bob's Input

b_input = input("Bob, enter your top secret uber secure message: ")
b_msg = b_input.encode('utf-8')
print()

#RSA Sign signature with keys from RSA key gen
signature = sign_message(keyPair, b_msg)

#Encrypt Bob's text using AES_GCM  with shared key form ECDH Key Exchange
ct= encrypt_AES_GCM(sharedKey, b_msg)

#Decrypt text using AES_GCM  with shared key form ECDH Key Exchange
dec_msg = decrypt_AES_GCM(sharedKey, ct)

print("Alice recieved message:", dec_msg.decode('utf-8'))

#RSA Verify signature with keys from RSA key gen
verify_message(keyPair, dec_msg, signature)
print('*************Transmission Complete*************')
