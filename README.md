# Encryptonator / Decryptonator
An encryption and decryption program that utilises AES-256-CBC 

The user message is padded with a padding character to make it a multiple of 16 before it is encrypted.
A random IV is generated and then stored, along with the encrypted message, in a text file at the same directory (filename was provided by the user). 
The decryption program asks the user for the filename and their key. It then extracts the IV and ciphertext from the file. 
Once the message is decrypted, the padding bits are removed and the original message is displayed to the user. 
