from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    encrypted_img = Image.new(img.mode, img.size)
    pixels = img.load()
    encrypted_pixels = encrypted_img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            # XOR encryption
            encrypted_pixels[i, j] = (r ^ key, g ^ key, b ^ key)

    encrypted_img.save("encrypted_image.png")
    print("Image encrypted and saved as 'encrypted_image.png'")

def decrypt_image(image_path, key):
    img = Image.open(image_path)
    decrypted_img = Image.new(img.mode, img.size)
    pixels = img.load()
    decrypted_pixels = decrypted_img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            # XOR decryption (same as encryption)
            decrypted_pixels[i, j] = (r ^ key, g ^ key, b ^ key)

    decrypted_img.save("decrypted_image.png")
    print("Image decrypted and saved as 'decrypted_image.png'")

print("Image Encryption/Decryption Tool")
choice = input("Do you want to Encrypt or Decrypt an image? (e/d): ").lower()
image_path = input("Enter the image file path (e.g., image.jpg): ")
key = int(input("Enter a numeric key (1-255): "))

if choice == 'e':
    encrypt_image(image_path, key)
elif choice == 'd':
    decrypt_image(image_path, key)
else:
    print("Invalid choice. Enter 'e' for encryption or 'd' for decryption.")
