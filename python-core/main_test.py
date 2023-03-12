from file.file_utils import write_bytes_to_file

if __name__ == '__main__':
    path_file = r'D:\WORK\Dev\Github\python\python-core\abc\data-file.txt'
    # content_byte = path_file.encode('utf-8')
    content_byte = bytes(path_file, 'utf-8')
    print(type(content_byte))
    write_bytes_to_file(path_file, content_byte)
    print("OK")
