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
