+**What take-away lessons did you learn in this experience?**
1. CTR and OFB, you don’t need to worry about padding.
1. CTR and OFB– use AES to generate numbers, XOR them into the plaintext
1. OFB uses serialization for encrypting blocks.
1. IV needs random and unique every iteration. 
1. If you encrypt the same image more than once, there should be differences
1. Do not use ECB exclusively.
**+Which of your modes is good enough for nation-state security?**
1. From what I understand, GCM mode, what's being sent through the block cipher doesn't actually depend on the data being encrypted.
**+How would you rate your effort on this project?**
1. I would rate this project as “easy” juxtapose to the Blackhat madness and the ECDHKE project (Proj 3).
**+How many hours were you able to give it?**
1. I spent less than five hours._

HOWTO:
This script will prompt you to enter one of three encytpion modes.
The image that I used for this exercise has been provided.
The read and write pathes may need to be updated to suite your envivronment.
Once a mode has been entered two files will be generated, an encrypted and decrypted version of the orignal file.
