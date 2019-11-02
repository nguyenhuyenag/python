import os, sys

# Open a file
path = "D:\\Note\\GDrive\\share\\python\\day-6"
dirs = os.listdir( path )

# This would print all the files and directories
for file in dirs:
   print(file)