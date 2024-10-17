from PIL import Image
import random

def encrypt_image(image_path, operation, value=None):
    # Open the image
    img = Image.open(image_path)
    pixels = list(img.getdata())
    
    if operation == 'swap':
        # Shuffle pixels randomly
        random.shuffle(pixels)
    elif operation == 'add':
        # Add a constant value to each pixel
        pixels = [(p[0] + value, p[1] + value, p[2] + value) for p in pixels]

    # Create a new image with the encrypted pixels
    encrypted_img = Image.new(img.mode, img.size)
    encrypted_img.putdata(pixels)
    
    return encrypted_img

def decrypt_image(encrypted_image, operation, value=None):
    pixels = list(encrypted_image.getdata())
    
    if operation == 'swap':
        # Sort pixels back to their original order (assuming a deterministic shuffle)
        random.shuffle(pixels)
    elif operation == 'add':
        # Subtract the constant value from each pixel
        pixels = [(p[0] - value, p[1] - value, p[2] - value) for p in pixels]

    # Create a new image with the decrypted pixels
    decrypted_img = Image.new(encrypted_image.mode, encrypted_image.size)
    decrypted_img.putdata(pixels)
    
    return decrypted_img

# User inputs
image_path = input("Enter the path to the image: ")
operation = input("Enter the operation (swap/add): ").lower()

if operation == 'add':
    value = int(input("Enter the value to add: "))
else:
    value = None

# Encrypt the image
encrypted_img = encrypt_image(image_path, operation, value)
encrypted_img.show()  # Display the encrypted image
encrypted_img.save("encrypted_image.png")  # Save the encrypted image

# Decrypt the image
decrypt_option = input("Do you want to decrypt the image? (yes/no): ").lower()
if decrypt_option == 'yes':
    decrypted_img = decrypt_image(encrypted_img, operation, value)
    decrypted_img.show()  # Display the decrypted image
    decrypted_img.save("decrypted_image.png")  # Save the decrypted image
else:
    print("Exiting the program.")