import os
import pathlib

# from pathlib import Path
# from os.path import exists

pathfile = "D:/Dev/Projects/Github/python/python-core/mysqldb/connectors.cnf"

# Using exists()
print(os.path.exists(pathfile))
# print(os.path.exists("file/data.txt"))

# Using isFile()
# print(os.path.isfile("file/data.txt"))
# print(os.path.isfile("file/data.txt"))

# Using is_file()
# print(pathlib.Path("data.txt").is_file())
# print(pathlib.Path("file/data.txt").is_file())
