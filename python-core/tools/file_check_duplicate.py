import os
import hashlib
from collections import defaultdict


def file_hash(path):
    sha256 = hashlib.sha256()
    with open(path, 'rb') as file:
        while chunk := file.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()


def find_duplicate_files(folder_path):
    file_hash_dict = defaultdict(list)

    # Iterate over all files in the folder
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            # Get the hash of the file content
            hash_value = file_hash(file_path)
            # Append the file path to the list associated with the hash
            file_hash_dict[hash_value].append(file_path)

    # Filter out unique files and keep only duplicates
    duplicate_files = {hash_value: file_paths for hash_value, file_paths in file_hash_dict.items() if
                       len(file_paths) > 1}

    return duplicate_files


# Specify the folder path
folder_path = r'D:\GoogleDrive\forshare\maple\api'

# Find duplicate files
duplicates = find_duplicate_files(folder_path)

# Print the duplicate files
if duplicates:
    for hash_value, file_paths in duplicates.items():
        print(f"Hash: {hash_value}")
        for file_path in file_paths:
            print(f"  - {file_path}")
else:
    print("No duplicate files found.")
