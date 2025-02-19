import cv2
import os

# Load Image
img = cv2.imread("mypic.jpg")  # Ensure correct file path
if img is None:
    print("Error: Image not found or unable to read!")
    exit()

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}

# Encrypting Message
n, m, z = 0, 0, 0
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n += 1
    m += 1
    z = (z + 1) % 3

# Save Encrypted Image
success = cv2.imwrite("encryptedImage.jpg", img)
if not success:
    print("Error: Could not save encryptedImage.jpg")
    exit()

print("Encryption successful! Image saved as encryptedImage.jpg")
os.system("start encryptedImage.jpg")  # Opens the image in default viewer

# Decryption
message = ""
n, m, z = 0, 0, 0
pas = input("Enter passcode for Decryption: ")

if password == pas:
    for i in range(len(msg)):
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3
    print("Decryption message:", message)
else:
    print("YOU ARE NOT AUTHORIZED!")
