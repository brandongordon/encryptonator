##Brandon Gordon : Student ID: 10447737
##Using Python 3.6.4

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

print ("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-(*)-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print ("\n\t\tWelcome to the Encrypt-o-nator")
print ("\n\t      A Program by Brandon Gordon")
print ("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-(*)-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

fileName = str(input("\nPlease provide a file name for this message: "))

key = os.urandom(32) #Generate a random 32bit number to use as the key
print ("\nThis is your key. Copy it and use it to decrypt the message later:\n")
print (key.hex()) #Print the hexadecimal string of the key 

iv = os.urandom(16) #Generate a random 16bit number to use as the IV
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend = default_backend())
encryptor = cipher.encryptor()

userMessage = input("\nType your message to be encrypted: ")
messageLength = len(userMessage) #Determine the length of the message... how much padding is needed
paddingAmount = messageLength % 16 #Padding amount calculation: How much is left over after you divide into 16
if paddingAmount != 0: #If the padding amount ISNT 0, it needs padding:
    userMessage = userMessage + ('`' * (16 - paddingAmount)) #Append the padding

encodedMessage = bytes(userMessage, 'utf-8') #Encode the message before encrypting it

cipherText = encryptor.update(encodedMessage) + encryptor.finalize() #Run it through the cipher

file = open(fileName + '.txt', 'w')
file.write(cipherText.hex() + '\n') #Write the cipher text as a hex string
file.write(iv.hex()) #Write the IV as a hex string
file.close()

print ("\n>>> Your message has been written to file. <<<")



