from cryptography.fernet import Fernet

# we will be encrypting the below string.
message = "This message will be encrypted"


# key = b'Lg6bv_b9XlJzOd8kS97jbjVYjk-n88n5z6pF2i9I4N0='
key = Fernet.generate_key()


fernet = Fernet(key)

encMessage = fernet.encrypt(message.encode())

print("original string  :", message)
print("encrypted string :", encMessage)


decMessage = fernet.decrypt(encMessage).decode()

print("decrypted string :", decMessage)
