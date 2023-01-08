import os
import pyAesCrypt

# Get the current working directory (the directory where the script is located)
directory = os.getcwd()

# Set the password that will be used to encrypt and decrypt the files
password = "your_password"

# Set the buffer size
buffer_size = 64 * 1024

# Iterate through all of the files in the directory
for file in os.listdir(directory):
    # Get the full path of the file
    file_path = os.path.join(directory, file)
    
    # Check if the file is a regular file (not a directory)
    if os.path.isfile(file_path):
        # Encrypt the file
        with open(file_path, "rb") as f:
            pyAesCrypt.encryptStream(f, open(file_path + ".aes", "wb"), password, buffer_size)

        # Delete the original unencrypted file
        os.remove(file_path)

print("All files in the directory have been encrypted!")
