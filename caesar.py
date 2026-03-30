def caesar_encrypt(message, shift):
    """
    Encrypts a message using Caesar Cipher.
    :param message: String to encrypt
    :param shift: Integer shift value (can be negative)
    :return: Encrypted string
    """
    result = ""
    shift = shift % 26  # Ensure shift is within 0-25
    for char in message:
        if char.isupper():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char
    return result

def caesar_decrypt(message, shift):
    """
    Decrypts a message using Caesar Cipher.
    :param message: String to decrypt
    :param shift: Integer shift value used for encryption
    :return: Decrypted string
    """
    return caesar_encrypt(message, -shift)

def main():
    while True:
        print("\n=== Caesar Cipher ===")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Quit")
        
        choice = input("Choose an option (1-3): ").strip()
        
        if choice == '3':
            print("Goodbye!")
            break
        
        if choice in ['1', '2']:
            message = input("Enter your message: ").strip()
            while True:
                try:
                    shift = int(input("Enter shift value (integer): ").strip())
                    break
                except ValueError:
                    print("Please enter a valid integer for shift.")
            
            if choice == '1':
                encrypted = caesar_encrypt(message, shift)
                print(f"Encrypted: {encrypted}")
            else:
                decrypted = caesar_decrypt(message, shift)
                print(f"Decrypted: {decrypted}")
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()

