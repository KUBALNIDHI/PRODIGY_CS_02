# 🖼️🔐 Image Encryption
This is a simple python program that encrypt and decrypt the image using pixel manipulation. It uses XOR-based encryption on each pixel’s RGB values to allow users to securely encrypt and decrypt images with a numeric key.
___

# 🧠 Features
🔐 Encrypt any image using pixel-wise XOR manipulation.

🔓 Decrypt encrypted images using the same key.

🖼️ Supports JPG, PNG, and other formats supported by PIL.

💻 Beginner-friendly Python implementation using the PIL library.

___

# 🛠️ Requirements
Python 3.x

Pillow library

____

# ⚙️ How It Works
1️⃣ Encryption:

🔹 Reads each pixel of the image.

🔹 Applies XOR with a numeric key (1-255) to each RGB value.

🔹Saves the encrypted image as encrypted_image.png.

2️⃣ Decryption:

🔹Reads the encrypted image.

🔹Applies XOR with the same key to retrieve the original image.

🔹Saves the decrypted image as decrypted_image.png.

____

💻 How to Run
---
1. **Clone this repository**
2. **Run the script**:
   ```bash
   python img_encryption.py


