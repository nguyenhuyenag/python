str = "Python Tutorial"

# Use 'in'
print("The string 'tut' is present in the string: ", "Tut" in str)

# Use '__contains__'
print("The string 'tut' is present in the string: ", str.__contains__('Tut'))

# Use 'find'
index = str.find('T')
if index != -1:
    print("The character 'T' is present in the string at: ", index)

# Use ''
count = str.count('o')
if count != 0:
    print(f"The character 'o' is present in the string {count} times.")
