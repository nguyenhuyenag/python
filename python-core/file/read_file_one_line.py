def read_file_into_list():
    file_contents = [line.strip() for line in open("data-file.txt", "r")]
    print(file_contents)


# read_file_into_list()

with open("data-file.txt") as file:
    file_content = [line.strip() for line in file]  # remove line breaks
    print(file_content)
