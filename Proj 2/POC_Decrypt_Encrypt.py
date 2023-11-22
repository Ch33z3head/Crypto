########################################
#           Jamie Grunewald
#      sript to get aquianted with
#         code concepts
########################################

from PIL import Image
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


img= Image.open('C:\cygwin64\home\Jamie\Crypto\Mod 3\Champs.png')
imgData = img.tobytes()


key = 'Jags will choke!'

# iv genterated from os.urandom(16)
iv= b'9\xb3>\xca\x14\xe0\xb5\xb9~\xeb\xff\x92%\xde\xf14'  

''' Decryption Modes
ECB
OFB
CBC
'''
cipher = AES.new(key.encode('utf8'), AES.MODE_ECB) 
#cipher = AES.new(key.encode('utf8'), AES.MODE_OFB, iv)
#cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, iv)

ct=cipher.encrypt(imgData)
img.frombytes(ct)

img.save("enc_Champs.png")


    
