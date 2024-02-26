import os
import pathlib

# from pathlib import Path
# from os.path import exists

pathfile = "D:/Dev/Projects/Github/python/python-core/mysql_/connectors.cnf"

# Using exists()
print(os.path.exists(pathfile))
# print(os.path.exists("path_file/data.txt"))

# Using isFile()
# print(os.path.isfile("path_file/data.txt"))
# print(os.path.isfile("path_file/data.txt"))

# Using is_file()
# print(pathlib.Path("data.txt").is_file())
# print(pathlib.Path("path_file/data.txt").is_file())
