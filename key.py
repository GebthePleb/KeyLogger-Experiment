from cryptography.fernet import Fernet

# generate a key
key = Fernet.generate_key()
with open('key.txt', 'wb') as f:
    f.write(key)
