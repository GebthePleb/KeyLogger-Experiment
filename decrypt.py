from cryptography.fernet import Fernet

# Get the key from the file
with open('key.txt', 'rb') as f:
    key = f.read()
    
#Creat a Fernet object with the key
fernet = Fernet(key)

filename = input('Enter the file name:')
with open(filename, 'rb') as f:
  ciphertext = f.read()
  
# Decrypt the ciphertext
text = fernet.decrypt(ciphertext)

# Write the content back to the file
with open(filename, 'wb') as f:
  f.write(text)