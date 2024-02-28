import os


def convert_bytes(num):
    """
        This function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
            # return f'{num}{unit}' if unit == 'bytes' else f'{num:.1f}{unit}'
        num /= 1024.0


def file_size(file_path):
    """
        This function will return the file size
    """
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)


def sizeof_fmt(file_path, suffix="B"):
    num = os.stat(file_path).st_size
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"


file_path = r"get_file_size.py"

print(file_size(file_path))
print(sizeof_fmt(file_path))
