from pathlib import PureWindowsPath, PurePosixPath

# Windows -> Posix
win = r'foo\bar\file.txt'
posix = str(PurePosixPath(PureWindowsPath(win)))
print(posix)  # foo/bar/file.txt

# Posix -> Windows
posix = 'foo/bar/file.txt'
win = str(PureWindowsPath(PurePosixPath(posix)))
print(win)  # foo\bar\file.txt
