# File Protection Utility

## Description

File Protection Utility is a Python application that securely encrypts and decrypts files using a cryptographic key. It protects sensitive data by converting file contents into an unreadable encrypted format and restores the original content only through authorized decryption.

## Features

* Encrypts files to protect confidential data.
* Decrypts encrypted files back to their original form.
* Automatically generates and stores a secure encryption key.
* Simple command-line interface.
* Fast and easy to use.
* Helps ensure data privacy and secure file storage.

## Technologies Used

* Python 3
* Cryptography (`cryptography` library)

## Requirements

* Python 3.x
* Cryptography library

Install the required package:

```bash
pip install cryptography
```

## How to Run

1. Save the program as `file_protection.py`.
2. Open a terminal in the project folder.
3. Install the required library:

   ```bash
   pip install cryptography
   ```
4. Run the program:

   ```bash
   python file_protection.py
   ```
5. Choose one of the following options:

   * **1** – Encrypt File
   * **2** – Decrypt File
   * **3** – Exit
6. Enter the file name when prompted.

## Example

### Menu

```text
===== File Protection Utility =====
1. Encrypt File
2. Decrypt File
3. Exit
Enter your choice:
```

### Encrypt File

Input:

```text
Enter your choice: 1
Enter file name: sample.txt
```

Output:

```text
File encrypted successfully!
```

### Decrypt File

Input:

```text
Enter your choice: 2
Enter file name: sample.txt
```

Output:

```text
File decrypted successfully!
```

## Project Structure

```text
File_Protection_Utility/
│── file_protection.py
│── secret.key
│── sample.txt
└── README.md
```

## Future Enhancements

* Password-based encryption and decryption.
* Support for encrypting multiple files at once.
* Graphical User Interface (GUI).
* File integrity verification.
* Secure key management and backup.

## Author

**Pravalika**
