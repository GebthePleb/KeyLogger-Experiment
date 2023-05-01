from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Get the key from the file
with open('private.pem', 'rb') as f:
    private_key = RSA.import_key(f.read())
    
filename = input('Enter the file name:')
with open(filename, 'rb') as f:
  ciphertext = f.read()
  
cipher = PKCS1_OAEP.new(private_key)
text = cipher.decrypt(ciphertext)

# Write the content back to the file
with open(filename, 'wb') as f:
  f.write(text)