pip install stepic
from PIL import Image
import stepic

#ENCRYPTION

original_img=Image.open('ogImg.png')

encoded_img=stepic.encode(original_img,b'INTERNET ACCESS')

encoded_img.save('img2.png')

encoded_img=Image.open('img2.png')

encoded_img.show()

#DECRYPTION

decoded_img=stepic.decode(encoded_img)
print(decoded_img)
