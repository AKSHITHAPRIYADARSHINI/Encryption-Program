def caesar_cipher(text, key, mode='encrypt'):
    result = []
    if mode == 'decrypt':
        key = -key  # Reverse key for decryption

    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            shifted_char = chr(((ord(char) - offset + key) % 26) + offset)
            result.append(shifted_char)
        else:
            result.append(char)
    return ''.join(result)

# Encryption
def encrypt(plaintext, key):
    return caesar_cipher(plaintext, key, mode='encrypt')

# Decryption
def decrypt(ciphertext, key):
    return caesar_cipher(ciphertext, key, mode='decrypt')

# Brute Force Attack
def brute_force(ciphertext):
    for key in range(26):
        decoded_text = decrypt(ciphertext, key)
        print(f"Key {key}: {decoded_text}")

# Menu
def menu():
    while True:
        print("\nChoose an option:")
        print("a. Encryption")
        print("b. Decryption")
        print("c. Brute Force Attack")
        print("d. Exit")
        choice = input("Enter your choice (a/b/c/d): ")

        if choice in {'a', 'b'}:
            text = input("Enter text: ")
            key = input("Enter key (numeric): ")

            if not key.isdigit():
                print("Invalid key! Please enter a numeric value.")
                continue

            key = int(key)

            if choice == 'a':
                result = encrypt(text, key)
                print(f"Ciphertext: {result}")
            else:
                result = decrypt(text, key)
                print(f"Decrypted plaintext: {result}")

        elif choice == 'c':
            ciphertext = input("Enter ciphertext: ")
            brute_force(ciphertext)

        elif choice == 'd':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice! Please select a, b, c, or d.")

if __name__ == "__main__":
    menu()
    