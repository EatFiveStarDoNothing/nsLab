import hashlib

# initializing string
str = "World Wide Web"
result = hashlib.sha256(str.encode())  #SHA256
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA256 is : ")
print(result.hexdigest())
print ("\r")

# initializing string
str = "transistor"
result = hashlib.sha384(str.encode())  #SHA384
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA384 is : ")
print(result.hexdigest())
print ("\r")

# initializing string
str = "Vacuum Tube"
result = hashlib.sha224(str.encode())  #SHA224()
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA224 is : ")
print(result.hexdigest())
print ("\r")

# initializing string
str = "NETWORK SECURITY"
result = hashlib.sha512(str.encode())  #SHA512
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA512 is : ")
print(result.hexdigest())
print ("\r")
