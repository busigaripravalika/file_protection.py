from cryptography.fernet import Fernet
import base64
import hashlib

# Generate a key from the password
def generate_key(password):
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

# Encrypt the file
def encrypt_file(filename, password):
    key = generate_key(password)
    cipher = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    encrypted_data = cipher.encrypt(data)

    with open(filename + ".enc", "wb") as file:
        file.write(encrypted_data)

    print("✅ File encrypted successfully!")
    print("Encrypted file:", filename + ".enc")

# Decrypt the file
def decrypt_file(filename, password):
    key = generate_key(password)
    cipher = Fernet(key)

    try:
        with open(filename, "rb") as file:
            encrypted_data = file.read()

        decrypted_data = cipher.decrypt(encrypted_data)

        output_file = filename.replace(".enc", "_decrypted.txt")

        with open(output_file, "wb") as file:
            file.write(decrypted_data)

        print("✅ File decrypted successfully!")
        print("Restored file:", output_file)

    except Exception:
        print("❌ Incorrect password or invalid encrypted file!")

# Main Menu
print("===== File Protection Utility =====")
print("1. Encrypt File")
print("2. Decrypt File")

choice = input("Enter your choice (1/2): ")

if choice == "1":
    filename = input("Enter file name (example: sample.txt): ")
    password = input("Enter password: ")
    encrypt_file(filename, password)

elif choice == "2":
    filename = input("Enter encrypted file name (example: sample.txt.enc): ")
    password = input("Enter password: ")
    decrypt_file(filename, password)

else:
    print("Invalid choice.")