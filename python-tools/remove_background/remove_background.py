from rembg import remove

input_path = 'input.png'
output_path = 'output.png'

try:
    with open(input_path, 'rb') as i, open(output_path, 'wb') as o:
        ipt = i.read()
        output = remove(ipt)
        o.write(output)
except IOError as e:
    print('Operation failed: %s' % e.strerror)
