def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

# User input for encryption
message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

# Encryption
encrypted_message = caesar_cipher_encrypt(message, shift)
print(f"Encrypted Message: {encrypted_message}")

# Option for decryption
choice = input("Do you want to decrypt a message? (yes/no): ").lower()

if choice == 'yes':
    text_to_decrypt = input("Enter the message to decrypt: ")
    shift_for_decryption = int(input("Enter the shift value: "))
    decrypted_message = caesar_cipher_decrypt(text_to_decrypt, shift_for_decryption)
    print(f"Decrypted Message: {decrypted_message}")
else:
    print("Exiting the program.")