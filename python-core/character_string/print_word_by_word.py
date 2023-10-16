import time

text = "Hello, this is ChatGPT. How can I assist you today?"

for char in text:
    print(char, end='', flush=True)
    time.sleep(0.05)  # Tạo một độ trễ nhỏ giữa các ký tự để giống ChatGPT

print()  # In một dòng mới sau khi hoàn thành
