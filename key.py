from Crypto.PublicKey import RSA

# Generate key pair
key = RSA.generate(2048)

# Save private key to file
with open('private.pem', 'wb') as f:
    f.write(key.export_key())

# Save public key to file
with open('public.pem', 'wb') as f:
    f.write(key.publickey().export_key())
