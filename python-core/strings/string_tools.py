import time
from random import shuffle

# Repeat a strings without for_loop
def repeat_string():
    s = "abc"
    print("repeate:", 4 * s)


def shuffle_string():
    s = "strings"
    l = list(s)
    shuffle(l)
    result = ''.join(l)
    print("Before:", s)
    print("After: ", result)

def print_word_by_word():
    text = "Hello, this is ChatGPT. How can I assist you today?"
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)  # Tạo một độ trễ nhỏ giữa các ký tự để giống ChatGPT
    print()  # In một dòng mới sau khi hoàn thành


if __name__ == '__main__':
    # repeat_string()
    # shuffle_string()
    print_word_by_word()
