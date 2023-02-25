import os

# Delete file
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file doesn't exist")

# Delete folder
os.rmdir("myfolder")
