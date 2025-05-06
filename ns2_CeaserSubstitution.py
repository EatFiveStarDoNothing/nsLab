def encrypt_text(plaintext,n):
    ans = ""
    # iterate over the given text
    for i in range(len(plaintext)):
        ch = plaintext[i]

        # check if space is there then simply add space
        if ch==" ":
            ans+=" "
            # check if a character is uppercase then encrypt it accordingly
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
            # check if a character is lowercase then encrypt it accordingly
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)

    return ans

def decrypt_text(ciphertext, n):
    ans = ""
    # iterate over the given text
    for i in range(len(ciphertext)):
        ch = ciphertext[i]

        # check if space is there then simply add space
        if ch == " ":
            ans += " "
            # check if a character is uppercase then decrypt it accordingly
        elif ch.isupper():
            ans += chr((ord(ch) - n - 65) % 26 + 65)
            # check if a character is lowercase then decrypt it accordingly
        else:
            ans += chr((ord(ch) - n - 97) % 26 + 97)

    return ans
plaintext = "thirdYear"
n = 3
print("Plain Text is  : " + plaintext)
print("Shift key is   : " + str(n))

print("Cipher Text is : " + encrypt_text(plaintext,n))
print("Original Text is : " + decrypt_text(encrypt_text(plaintext,n),n))



# -------------------------------------------- 2.2. substition cipher -------

import string
# A list containing all characters
all_letters= string.ascii_letters
# all_letters= string.ascii_letters + string.digits + string.punctuation + " "
# print("Encryption performed on :", all_letters)
dict1 = {}
key = 3
for i in range(len(all_letters)):
    dict1[all_letters[i]] = all_letters[(i+key)%len(all_letters)]
plain_txt= "this text will be encrypted"
print("Plain Text is        :",plain_txt)

cipher_txt=[]
# loop to generate ciphertext
for char in plain_txt:
    if char in all_letters:
        temp = dict1[char]
        cipher_txt.append(temp)
    else:
        temp =char
        cipher_txt.append(temp)

cipher_txt= "".join(cipher_txt)
print("Cipher Text is       :",cipher_txt)
print("Shift key is         :", key)
dict2 = {}
for i in range(len(all_letters)):
    dict2[all_letters[i]] = all_letters[(i-key)%(len(all_letters))]
# loop to recover plain text
decrypt_txt = []
for char in cipher_txt:
    if char in all_letters:
        temp = dict2[char]
        decrypt_txt.append(temp)
    else:
        temp = char
        decrypt_txt.append(temp)

decrypt_txt = "".join(decrypt_txt)
print("Recovered plain text :", decrypt_txt)

# print(dict1)
