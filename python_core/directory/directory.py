import shutil
import os
from os import path
from os.path import dirname, abspath

# Get Current Directory in Python
print(os.getcwd())

d = dirname(dirname(abspath(__file__)))
print(d)

d = path.dirname(path.dirname(__file__))
print(d)

os.mkdir('test')

# rename a directory
os.rename('test','new_one')

# delete the empty directory "mydir"
os.rmdir("mydir")

# delete "mydir" directory and all of its contents
shutil.rmtree("mydir")