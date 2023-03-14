import filecmp
import os
from os import path


# Check two file prefer
def compare_file():
    f1 = r'C:\Users\huyennv\Desktop\test\test1.txt'
    f2 = r'C:\Users\huyennv\Desktop\test\test2.txt'

    # print("samefile:", path.samefile(f1, f2))
    # print("stat:", os.stat(f1) == os.stat(f2))

    # shallow comparison
    result = filecmp.cmp(f1, f2)
    print(result)

    # deep comparison
    result = filecmp.cmp(f1, f2, shallow=False)
    print(result)


# def compare_directory():
#     d1 = r'C:\Users\huyennv\Desktop\test\folder1'
#     d2 = r'C:\Users\huyennv\Desktop\test\folder1'
#     files = [] # ['test.txt']
#
#     # shallow comparison
#     match, mismatch, errors = filecmp.cmpfiles(d1, d2, files)
#     print('Shallow comparison')
#     print("Match:", match)
#     print("Mismatch:", mismatch)
#     print("Errors:", errors)
#
#     # deep comparison
#     match, mismatch, errors = filecmp.cmpfiles(d1, d2, files, shallow=False)
#     print('Deep comparison')
#     print("Match:", match)
#     print("Mismatch:", mismatch)
#     print("Errors:", errors)


compare_file()
# compare_directory()
