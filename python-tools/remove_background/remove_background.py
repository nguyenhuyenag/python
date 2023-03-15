from pathlib import Path

import cv2
from rembg import remove, new_session


def method_name():
    try:
        with open(input_path, 'rb') as i, open(output_path, 'wb') as o:
            ipt = i.read()
            output = remove(ipt)
            o.write(output)
    except IOError as e:
        print('Operation failed: %s' % e.strerror)


def method_name2():
    input = cv2.imread(input_path)
    output = remove(input)
    cv2.imwrite(output_path, output)


def method3():
    session = new_session()
    for file in Path('path/to/folder').glob('*.png'):
        ipt_path = str(file)
        opt_path = str(file.parent / (file.stem + ".out.png"))

        with open(ipt_path, 'rb') as i:
            with open(opt_path, 'wb') as o:
                ipt = i.read()
                output = remove(ipt, session=session)
                o.write(output)


input_path = 'input.jpg'
output_path = 'output.jpg'

# method_name()
method_name2()
print("Done")
