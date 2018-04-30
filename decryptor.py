##Brandon Gordon : Student ID: 10447737
##Using Python 3.6.4

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

print ("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-(*)-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print ("\n\t\tWelcome to the Decrypt-o-nator")
print ("\n\t      A Program by Brandon Gordon")
print ("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-(*)-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

fileName = str(input("\nPlease provide file name of message to be decrypted: "))

file = open(fileName + '.txt', "r")
cipherText = file.readline()
iv = file.readline()
file.close()

cipherText = cipherText[:-1] #Remove the \n
cipherText = bytes.fromhex(cipherText) #Convert the cipher text hex string back to bytes
iv = bytes.fromhex(iv) #Convert the IV hex string back to bytes

key = input("\nPlease provide a key to decrypt the message (Should be copied from before!): ")
key = bytes.fromhex(key) #Convert the key hex string back to bytes

cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend = default_backend())
decryptor = cipher.decryptor()

paddedMessage = decryptor.update(cipherText) + decryptor.finalize()

userMessage = bytes.decode(paddedMessage).replace('`', '') #Convert the message from bytes back to utf-8 and replace padding character with nothing (remove padding char)

print ('\n>>> Decrypting Message... <<<\n', userMessage)


