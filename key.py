from cryptography.fernet import Fernet

# generate a key
key = Fernet.generate_key()
print(key)