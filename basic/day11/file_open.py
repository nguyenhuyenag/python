import rs

try:
    f = open(rs.getPath() + "/file/data.txt")
    f.write("Lorum Ipsum")
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()
