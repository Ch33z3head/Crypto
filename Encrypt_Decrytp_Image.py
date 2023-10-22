from PIL import Image
from Crypto.Cipher import AES
import hashlib
import os

def get_key():
    key = 'Jags will choke!'
    secret_key = hashlib.sha256(key.encode('UTF-8')).digest()
    return secret_key

def get_iv():
    #Initallization Vector
    iv =os.urandom(16)
    return iv


def encrypt_image(in_mode, secret_key, iv):
    mode = in_mode.upper()
    img= Image.open('C:\cygwin64\home\Jamie\Crypto\Mod 3\Champs.png')
    
    imgData = img.tobytes()   
     
    if mode == "ECB":
        cipher = AES.new(secret_key, AES.MODE_ECB) 
    elif mode == "OFB":
        cipher = AES.new(secret_key, AES.MODE_OFB, IV=iv)
    elif mode == "GCM":
        cipher = AES.new(secret_key, AES.MODE_GCM, nonce=iv)
    else:
        print("Nothing was encrytped.")
   
    ct=cipher.encrypt(imgData)
    img.frombytes(ct)
    
    img.save("C:\cygwin64\home\Jamie\Crypto\Mod 3\ENC_"+mode+"_Champs.png")    
    print("Encrytped file was saved.")   
    return 

def decrypt_image(in_mode, secret_key, iv):
    mode = in_mode.upper()
    enc_Image=Image.open("C:\cygwin64\home\Jamie\Crypto\Mod 3\enc_"+mode+"_Champs.png")
    imgbytes = enc_Image.convert("RGB").tobytes()
    
    if mode == "ECB":
        cipher = AES.new(secret_key, AES.MODE_ECB) 
    elif mode == "OFB":
        cipher = AES.new(secret_key, AES.MODE_OFB, IV=iv)
    elif mode == "GCM":
        cipher = AES.new(secret_key, AES.MODE_GCM, nonce=iv)
    else:
        print("Nothing was decrytped.")
    
    decbytes =  cipher.decrypt(imgbytes)
    
    dec_image = Image.frombytes("RGB", enc_Image.size, decbytes)
    dec_image.save("C:\cygwin64\home\Jamie\Crypto\Mod 3\DEC_"+mode+"_Champs.png")
    print("Decrytped file was saved.")
    return

print("********************************************")
print("*                                          *")
print("* Please use three of the following modes: *")
print("*              ECB, OFB, GCM               *")            
print("*           By: Jamie Grunewald            *")
print("*                                          *")
print("********************************************")


input_mode= input("Please enter encrytion mode: ")

UPPR_mode = input_mode.upper()

if UPPR_mode == 'ECB':
    in_mode = input_mode
elif UPPR_mode.upper() =='OFB':
    in_mode = input_mode.upper()
elif UPPR_mode.upper() == 'GCM':
    in_mode = input_mode
else:
    print("You have not selected the proper mode, try again!")

secret_key = get_key()
iv = get_iv()
encrypt_image(in_mode, secret_key, iv)
decrypt_image(in_mode, secret_key, iv)
