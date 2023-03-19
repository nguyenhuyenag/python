"""
    The with statement clarifies code that previously would use try...finally blocks to ensure that clean-up code is executed

    The with statement is a control-flow structure whose basic structure is:

    with expression [as variable]:
        with-block
"""


def open_multiple_files():
    with open('data') as input_file, open('result', 'w') as output_file:
        for line in input_file:
            pass


with open('output.txt', 'w') as f:
    f.write('Hi there!')
