dict = {}

text = "VOZ tạm ngưng hoạt động một số dịch vụ, để xử lý một số vấn đề tương thích hệ thống"
arr = text.rstrip().split()
for k in arr:
    if k not in dict:
        dict[k] = 1
    else:
        dict[k] += 1

print(dict)

# for k, v in dict.items():
#     print(k, "\t=>", v)
