Encryption & Decryption Tool (Command-Line Program)

## **Overview**
This project implements a command-line program that performs encryption and decryption using multiple classical and modern cryptographic techniques covered in Lab 2. The system supports substitution ciphers, transposition ciphers, Vigenère, AES, DES, and 3DES under various encryption modes.

---

## **Implemented Algorithms**

### **Substitution Ciphers**
- Shift (Caesar) Cipher  
- Permutation Cipher  

### **Transposition Ciphers**
- Simple Transposition  
- Double Transposition  

### **Polyalphabetic Cipher**
- Vigenère Cipher  

### **Modern Algorithms**
- AES-128  
- DES  
- 3DES  

### **Supported Modes**
- ECB  
- CBC  
- CFB  
- OFB  
- CTR  

---

## **Features**
✔ Encrypt & decrypt  
✔ Default or custom keys  
✔ Supports multiple cipher types  
✔ Clear menu-driven interface  
✔ Uses Python's `cryptography` library for modern algorithms  

---

## **Usage**
### **Run the tool**
```bash
python crypto_tool.py
Requirements
Install dependencies:

bash
Copy code
pip install cryptography
Challenges Encountered
Understanding AES/DES block operations and key scheduling

Ensuring secure IV and key handling

Input validation for plaintext and keys

Debugging multi-step encryption functions

Managing performance for large messages

Conclusion
This assignment provided hands-on experience implementing both classical and modern cryptography algorithms. The modular design, improved error handling, and secure key/IV usage make the tool extensible and practical for educational use.

ASCII Shifting Logic

Python Control Structures

📄 License

This project is created for Introduction to Information Security coursework.
