from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# Generate RSA key pair
private_key = rsa.generate_private_key(public_exponent=65537,key_size=1024)
public_key = private_key.public_key()

# Serialize and save the keys
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

print("Private Key:")
print(private_pem.decode())
print("Public Key:")
print(public_pem.decode())

# Encryption function
def encrypt_message(message, public_key):
    encrypted = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted

# Decryption function
def decrypt_message(encrypted_message, private_key):
    decrypted = private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted.decode()
# usage
message = "thirdYear"
encrypted_msg = encrypt_message(message, public_key)
print("Encrypted Message:", encrypted_msg)
decrypted_msg = decrypt_message(encrypted_msg, private_key)
print("\nDecrypted Message:", decrypted_msg)
