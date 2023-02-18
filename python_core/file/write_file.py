# To write to an existing file, you must add a parameter to the open() function:
#   'x' - Create, will create a file, returns an error if the file exist
#   'a' - Append, will append to the end of the file
#   'w' - Write, will overwrite any existing content

f = open("data-file.txt", "w")
f.write("Now the file has more content!\n")
f.close()
