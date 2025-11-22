# **Caesar Cipher Encryption Program**
A simple Python program that performs **Encryption**, **Decryption**, and **Brute-Force Attacks** using the classical **Caesar Cipher** technique.

---

## ⭐ **Overview**
The Caesar Cipher shifts each letter of the alphabet by a fixed key.  
This program demonstrates:

- ✔ **Encrypting** plaintext  
- ✔ **Decrypting** ciphertext  
- ✔ **Brute force attack** (trying all 26 keys)  
- ✔ Menu-driven interface  
- ✔ Case sensitivity (keeps uppercase/lowercase)  
- ✔ Preserves spaces, numbers, and punctuation  

---

## 🚀 **Features**
- **Encryption:** Shifts letters forward by the key  
- **Decryption:** Reverses the shift using the key  
- **Brute Force:** Tests all possible keys (0–25)  
- **Error Handling:** Warns for invalid key inputs  
- Works on **Windows, macOS, and Linux**

---

## 📂 **Files Included**
caesar_cipher.py
README.md


---

## 🛠️ **How to Run the Program**

### 1. Save the Script
Save the Python code as:



caesar_cipher.py


### 2. Open Terminal / Command Prompt
Navigate to the folder:

```bash
cd path/to/your/file

3. Run the Program
python caesar_cipher.py


or

python3 caesar_cipher.py

📌 Usage Example
Encryption
Enter text: HacK
Enter key: 3
Ciphertext: KdfN

Decryption
Enter text: KdfN
Enter key: 3
Decrypted plaintext: HacK

Brute Force Attack
Enter ciphertext: KdfN
Key 0: KdfN
Key 1: JceM
Key 2: IbdL
Key 3: HacK   <-- correct key
...

🧠 Concepts Demonstrated

Classical Cryptography

Substitution Ciphers

Brute-force Cryptanalysis

ASCII Shifting Logic

Python Control Structures

📄 License

This project is created for Introduction to Information Security coursework.